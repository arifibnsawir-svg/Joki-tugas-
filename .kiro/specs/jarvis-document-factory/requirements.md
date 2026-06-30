# Requirements Document

## Introduction

The Jarvis Document Factory is a single cohesive capability (delivered as a Jarvis skill) that lets Jarvis produce three document formats reliably and at one-shot quality: PowerPoint (PPTX), Word (DOCX), and PDF. It encodes the method proven on this project, where the assistant produced academic books, a teaching module, and an interview report that all passed deterministic QA and satisfied the client.

The capability is built on one principle: the language model never hand-writes a binary document. Instead the model emits a structured specification (the SPEC), and deterministic renderers turn that SPEC into files. A deterministic gate decides whether the output is acceptable, not the model. Two always-on conventions, the humanizer and cite-or-abstain, apply across every artifact. For large multi-step jobs, the orchestrator may delegate focused work to sub-agents when the cost is justified.

This feature aligns with Jarvis's existing architecture: a thinking/representation layer before execution, a four-stage execution loop (Audit, Rancang, Sistemasi, Iterasi), and a hard separation between a lightweight Router and a deterministic Gate.

### In Scope

- SPEC-first generation contract for documents.
- PPTX, DOCX, and PDF renderers driven by one shared SPEC.
- A deterministic output gate that returns PASS or FAIL.
- Humanizer and cite-or-abstain as cross-cutting always-on layers.
- Image and anti-hallucination handling.
- Optional sub-agent delegation for large jobs.
- Academic formatting defaults and reproducibility constraints.

### Out of Scope

- Rebuilding or replacing Jarvis's model router.
- Any output format other than PPTX, DOCX, and PDF.


## Glossary

- **Document_Factory**: The skill that turns a document request into a finished PPTX, DOCX, or PDF file through the SPEC-first pipeline.
- **Representation_Layer**: The thinking stage that converts a raw request into structured entities, measures, relations, and an output specification before any rendering begins.
- **SPEC**: The structured, machine-readable description of a document (for example JSON) containing identity, sections, content blocks, tables, figures, and references. The single source of truth for all renderers.
- **Spec_Builder**: The language-model component that produces the SPEC from a request.
- **Renderer**: A deterministic component that consumes a SPEC and produces a file. Specific renderers are the PDF_Renderer, DOCX_Renderer, and PPTX_Renderer.
- **PDF_Renderer**: The deterministic renderer that produces PDF output from HTML and CSS using WeasyPrint.
- **DOCX_Renderer**: The deterministic renderer that produces DOCX output using python-docx.
- **PPTX_Renderer**: The deterministic renderer that produces designed 16:9 PPTX output using the house render_deck.py built on python-pptx.
- **Output_Gate**: The deterministic Python component that inspects a rendered file and returns PASS or FAIL against defined checks. The sole authority for declaring an output finished.
- **Router**: The lightweight component that selects the route for a request and never blocks input.
- **Humanizer_Layer**: The always-on transformation that removes signs of AI writing from all generated prose.
- **Citation_Layer**: The always-on cite-or-abstain policy applied to academic artifacts.
- **Image_Resolver**: The component that maps figure references in a SPEC to verified existing file paths.
- **Orchestrator**: The component that plans a job and decides whether to delegate subtasks to sub-agents.
- **Worker**: A focused sub-agent that executes a delegated subtask under a self-contained brief with explicit PASS or FAIL criteria.
- **Humanizer_Clean**: A property of text that contains zero em-dashes, zero en-dashes, zero curly or smart quotes, and zero emoji.
- **Academic_Artifact**: A document that contains scholarly claims, citations, or a reference list.


## Requirements

### Requirement 1: Multi-Format Document Output

**User Story:** As Arif, I want Jarvis to produce PPTX, DOCX, and PDF documents from a single request, so that I get the format I need without switching tools or losing quality.

#### Acceptance Criteria

1. WHEN a document request specifies the PPTX format, THE Document_Factory SHALL produce a PPTX file.
2. WHEN a document request specifies the DOCX format, THE Document_Factory SHALL produce a DOCX file.
3. WHEN a document request specifies the PDF format, THE Document_Factory SHALL produce a PDF file.
4. WHEN a document request specifies more than one of the PPTX, DOCX, and PDF formats, THE Document_Factory SHALL produce one file per requested format from the same SPEC.
5. IF a document request specifies a format other than PPTX, DOCX, or PDF, THEN THE Document_Factory SHALL return an unsupported-format error that names the three supported formats.
6. WHERE two or more formats are produced from one SPEC, THE Document_Factory SHALL keep the document identity, section order, and reference list consistent across those formats on a best-effort basis.
7. IF a consistency aspect cannot be matched across formats, THEN THE Document_Factory SHALL still produce the requested files and SHALL report which consistency aspect was not matched.


### Requirement 2: Structure-Before-Render Contract

**User Story:** As Arif, I want the model to emit a structured SPEC first and let a deterministic renderer build the file, so that output is reproducible and the model never hand-writes a binary document.

#### Acceptance Criteria

1. WHEN a document request is accepted, THE Spec_Builder SHALL produce a SPEC before any Renderer runs.
2. THE SPEC SHALL contain document identity, an ordered list of sections, content blocks, tables, figures, and references.
3. WHEN a Renderer produces a file, THE Renderer SHALL derive that file only from the SPEC.
4. IF the SPEC is missing a field required by the requested format, THEN THE Document_Factory SHALL return a SPEC-validation error that names the missing field before rendering.
5. THE Document_Factory SHALL restrict each Renderer to read document content only from the SPEC and the verified file paths that the SPEC references.
6. WHEN the same SPEC is rendered more than once for the same format with the same renderer version and assets, THE Renderer SHALL produce byte-equivalent output.


### Requirement 3: One SPEC, Multiple Mirrored Renderers

**User Story:** As Arif, I want each format rendered by its own dedicated renderer from the shared SPEC, so that I can pick the best library for each format while keeping outputs aligned.

#### Acceptance Criteria

1. THE PDF_Renderer SHALL render the SPEC to PDF using HTML and CSS through WeasyPrint.
2. THE DOCX_Renderer SHALL render the SPEC to DOCX using python-docx.
3. THE PPTX_Renderer SHALL render the SPEC to a designed 16:9 deck using the house render_deck.py.
4. THE PPTX_Renderer SHALL apply the house deck style, including an accent color, an accent bar, a footer, page numbers, and varied layouts covering cover, section, bullets, two-column, and closing.
5. WHERE a document request asks for plain default slides without an explicit minimal-style instruction, THE PPTX_Renderer SHALL apply the house designed deck style.
6. WHERE a document request explicitly instructs minimal or plain slide formatting, THE PPTX_Renderer SHALL apply the requested minimal style.
7. WHEN the DOCX_Renderer renders a SPEC, THE DOCX_Renderer SHALL apply the PDF-style layout, including one page break per chapter and a PAGE field in the footer, whether or not a PDF was also rendered.


### Requirement 4: Deterministic Output Gate

**User Story:** As Arif, I want a deterministic script to decide PASS or FAIL on every rendered file, so that the model cannot declare a document finished on its own.

#### Acceptance Criteria

1. WHEN a Renderer produces a file, THE Output_Gate SHALL inspect that file and return PASS or FAIL.
2. THE Document_Factory SHALL treat an output as finished only after the Output_Gate returns PASS.
3. WHILE the Output_Gate has not returned PASS for an output, THE language model SHALL describe that output as awaiting gate rather than as done.
4. IF the Output_Gate returns FAIL, THEN THE Output_Gate SHALL return the list of failed checks with a description of each failure.
5. WHEN the Output_Gate returns FAIL, THE Document_Factory SHALL route the failed checks back to the Iterasi stage for correction before re-rendering.
6. THE final authority to declare an output done SHALL rest with the Output_Gate, and the language model SHALL at most propose the awaiting-gate state.


### Requirement 5: Gate Verification Checks

**User Story:** As Arif, I want the gate to verify the specific defects that broke past documents, so that recurring problems are caught before delivery.

#### Acceptance Criteria

1. THE Output_Gate SHALL verify that the required structure for the document type is present and in the expected order.
2. THE Output_Gate SHALL verify citation-to-reference consistency in both directions, so that every in-text citation has a reference entry and every reference entry is cited in the text.
3. THE Output_Gate SHALL verify that the rendered text is Humanizer_Clean.
4. THE Output_Gate SHALL verify that the document contains no blank page and no near-empty page.
5. THE Output_Gate SHALL verify that the document contains no dangling heading.
6. THE Output_Gate SHALL run the table-of-contents verification on every document, and WHERE a document contains a table of contents, THE Output_Gate SHALL verify that the table of contents fits its allotted space and that its page numbers match the rendered pages.
7. THE Output_Gate SHALL verify that every rendered image resolves to a real existing file path.


### Requirement 6: Humanizer Always-On Layer

**User Story:** As Arif, I want the humanizer applied to every artifact by default, so that all output reads as natural human prose without AI tells.

#### Acceptance Criteria

1. THE Document_Factory SHALL apply the Humanizer_Layer to the prose of every artifact by default.
2. THE Humanizer_Layer SHALL produce text that is Humanizer_Clean.
3. WHEN prose contains an em-dash, an en-dash, a curly or smart quote, or an emoji, THE Humanizer_Layer SHALL replace that character so that the text becomes Humanizer_Clean.
4. THE Humanizer_Layer SHALL preserve the meaning and coverage of the original prose while removing AI writing patterns.
5. IF a rendered artifact is not Humanizer_Clean, THEN THE Output_Gate SHALL return FAIL for the humanizer check.


### Requirement 7: Cite-or-Abstain Always-On Layer

**User Story:** As Arif, I want every citation in academic work to be verifiable and never fabricated, so that the documents hold up to scrutiny.

#### Acceptance Criteria

1. WHERE an artifact is an Academic_Artifact, THE Citation_Layer SHALL require that every citation references a verifiable source.
2. THE Citation_Layer SHALL format references in APA style for Academic_Artifacts.
3. WHEN sources of comparable relevance are available, THE Citation_Layer SHALL prefer Indonesian sources before international sources.
4. IF a claim cannot be supported by a verifiable source, THEN THE Citation_Layer SHALL drop that claim from the artifact.
5. THE Citation_Layer SHALL exclude any source identifier, including a DOI or a link, that cannot be verified.
6. WHEN an Academic_Artifact is rendered, THE Output_Gate SHALL verify citation-to-reference consistency in both directions.


### Requirement 8: Image and Anti-Hallucination Handling

**User Story:** As Arif, I want images to come only from real files, so that documents never contain hallucinated or invented visuals.

#### Acceptance Criteria

1. WHEN the SPEC references a figure, THE Image_Resolver SHALL resolve that figure to a file path that exists on disk.
2. IF a figure reference resolves to a path that does not exist, THEN THE Document_Factory SHALL return a missing-image error that names the unresolved reference before rendering.
3. THE Renderer SHALL embed only images whose file paths the Image_Resolver has verified.
4. THE Document_Factory SHALL exclude any image that the Image_Resolver cannot map to a verified existing file path.
5. WHEN a rendered file is inspected, THE Output_Gate SHALL verify that every embedded image corresponds to a verified existing file path.


### Requirement 9: Router and Gate Separation

**User Story:** As Arif, I want a lightweight router to pick the route and a deterministic gate to guard the output, so that input is never blocked and the finish decision stays deterministic.

#### Acceptance Criteria

1. WHEN a document request arrives, THE Router SHALL select the generation route without blocking the input.
2. THE Router SHALL limit its responsibility to route selection and SHALL leave the finished decision to the Output_Gate.
3. THE Output_Gate SHALL run only at the output point and SHALL produce the finished decision deterministically.
4. THE Document_Factory SHALL keep the Router and the Output_Gate as separate components.
5. WHILE a request is being processed, THE Document_Factory SHALL run the four-stage execution loop of Audit, Rancang, Sistemasi, and Iterasi.


### Requirement 10: Optional Sub-Agent Delegation

**User Story:** As Arif, I want the orchestrator to delegate large multi-step jobs to focused workers when worthwhile, so that heavy work scales without over-delegating small tasks.

#### Acceptance Criteria

1. WHERE a job is large and multi-step, THE Orchestrator MAY delegate subtasks to one or more Workers.
2. WHEN the Orchestrator delegates a subtask, THE Orchestrator SHALL give the Worker a self-contained brief and explicit PASS or FAIL criteria.
3. THE Router SHALL decide whether delegation is worth the cost for a given job.
4. WHERE a task is small, THE Orchestrator SHALL execute the task directly rather than delegating it.
5. WHEN a Worker returns a result, THE Orchestrator SHALL evaluate that result against the PASS or FAIL criteria stated in the brief before accepting it.


### Requirement 11: Academic Formatting Defaults

**User Story:** As Arif, I want academic documents to follow the proven formatting defaults, so that output matches institutional expectations without manual tuning.

#### Acceptance Criteria

1. WHERE an artifact is an Academic_Artifact and no override is given, THE Document_Factory SHALL apply A4 page size, Times New Roman at 12 point, line spacing of 1.5, justified body text, and Arabic page numbers.
2. WHERE a document request specifies a font, margin, or spacing value, THE Document_Factory SHALL apply the specified value instead of the default.
3. WHEN the PDF_Renderer builds a table of contents, THE PDF_Renderer SHALL use CSS target-counter without any counter-reset and SHALL set hyphens to none so that line breaks match the DOCX output.
4. WHEN the DOCX_Renderer builds the document, THE DOCX_Renderer SHALL apply one page break per chapter and a PAGE field in the footer.
5. WHERE a PDF was rendered from the same SPEC, THE DOCX_Renderer SHALL set the table-of-contents page numbers from the scanned page numbers of that PDF, and THE Document_Factory SHALL render the PDF before the DOCX.


### Requirement 12: Reproducibility, Skill Form, and Tight Scope

**User Story:** As Arif, I want the capability delivered as a lightweight no-restart skill with reproducible output and tight scope, so that Jarvis gains the ability without over-engineering or downtime.

#### Acceptance Criteria

1. THE Document_Factory SHALL be delivered as a Jarvis skill that loads without restarting Jarvis.
2. WHEN the same SPEC, renderer version, and assets are used, THE Document_Factory SHALL produce reproducible output for each format.
3. THE Document_Factory SHALL support only the PPTX, DOCX, and PDF formats and SHALL exclude any other format.
4. THE Document_Factory SHALL reuse the existing Humanizer_Layer, Citation_Layer, and house render_deck.py rather than reimplementing them.
5. WHERE a single deterministic renderer and gate satisfy a requirement, THE Document_Factory SHALL use that single path rather than adding a separate engine.
