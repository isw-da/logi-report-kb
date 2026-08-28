# Logi Report, Composer and Simba Intelligence: what actually connects

Built 27 August 2026 from the Confluence LR space. Every claim cites a page id.
This exists because the question "are our business views transferable?" comes up
in renewal and expansion conversations and the answer that gets given in calls is
usually "they're just two products", which is now out of date.

## The headline, and it runs the opposite way to what people assume

There **is** an active engineering programme connecting Composer and Logi Report.
It converts **Composer Sources into Logi Report Catalog resources**, not the
other way round.

| Work | Page | Last modified |
|---|---|---|
| Composer Source to Logi Report Conversion, overview and framework (JREP-37805) | `confluence:18324881413` (doc index) | 9 Aug 2026 |
| Composer Source Import: Add Table design, shared table reuse/update/merge | `confluence:18674515989` | 24 Aug 2026 |
| Security design: Translate Composer to BV (JREP-38028) | `confluence:18490097665` | 30 Jul 2026 |
| Security enhance design: Translate Composer to BV, **phase 2** (JREP-38758) | `confluence:18653446166` | 18 Aug 2026 |
| Derived Field conversion capabilities and audit guide (JREP-37724) | `confluence:18568675443` | 23 Jul 2026 |
| Composer Global Filters to Logi BV Prefilter | `confluence:18569494588` | 21 Jul 2026 |
| Composer Source Import into Logi Report Catalog, **demo guide** | `confluence:18500812891` | 2 Jul 2026 |

**Direction of travel: Composer Source → Logi Report Catalog / Business View.**
The conversion covers datasource, connection, query, Business View, derived
fields, global filters, and security (RLS and CLS) mapping from Composer Accounts
to Logi Organizations.

## What this means when a customer asks the transferability question

If a long-standing Logi Report customer asks "we have built all these Business
Views, can we move them to Composer or Simba Intelligence", the honest answer in
August 2026 is:

- **Not by a supported export.** The tooling being built goes Composer → Logi
  Report, so it does not solve moving Logi Report BVs outward.
- **The practical answer is to connect to the same underlying data.** Simba
  Intelligence queries the data directly, so the modelling work in Logi Report
  BVs is not migrated so much as bypassed. Different use case, different
  definitions, different context window.
- **Do not promise a BV export path.** Nothing in the LR space describes one.

## Known limitations in the security translation, worth knowing before you promise parity

From `confluence:18653446166` (phase 2), the current implementation records these
limits explicitly:

- **CLS `onCondition` has no dynamic equivalent.** Behaviour is a warning, then
  the condition is ignored and a static list applied. Risk recorded as
  *medium to high*, because condition distortion can widen or narrow field access.
- **RLS Dynamic User Attribute has no target context yet.**

That second point matters: an unqualified "security rules come across" claim is
not supportable today.

## Other API artefacts found

- **Postman collection** attached to the Composer Source Import demo guide:
  `LogiReport-API-collection.postman_collection.json`
  (`confluence:18500812891`, attachment id `att18502090755`). Worth pulling if a
  request-level example set is needed alongside the OpenAPI spec.

## What was NOT found, stated so nobody assumes it exists

No page in the LR space describes a **Logi Report to Simba Intelligence** direct
integration, and no page describes exporting Logi Report Business Views to
Composer. The searches run were: `space = LR AND (text ~ "Simba Intelligence" OR
text ~ "Composer Source" OR (text ~ "business view" AND text ~ "import"))`,
returning 8 results, all listed above. Absence here is absence of evidence in one
space, not proof that nothing exists anywhere.
