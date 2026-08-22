# Demo recipes

End-to-end walkthroughs of the reports a presales demo actually shows. Every step
traces to a source document. Where the corpus does not cover something, it says so
rather than guessing.

All the tutorial recipes use two shipped catalogs: `JinfonetGourmetJava.cat` in
`<install_root>\Demo\Reports\JinfonetGourmetJava` (queries, page reports) and
`SampleReports.cat` with the `WorldWideSalesBV` business view (web reports, ad
hoc). Finished versions of every tutorial report live in
`<install_root>\Demo\Reports\TutorialReports`, which is the documented way to check
your build against the intended result.

---

## Recipe 1: Regional sales, table to crosstab to chart, as a web report

The classic ask. Build it as a web report, because the conversion between table,
crosstab and chart is the thing worth watching. Two documented routes. Route A is
the fastest thing on screen; route B is the one that gets you sales by quarter.

### Route A: quick start, about five minutes

Follows
[Lesson 1: Creating a web report using the quick start method](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519967383-lesson-1-creating-a-web-report-using-the-quick-start-method.md)
step for step.

1. Server Console Start Page > **Create** > **Web Report**.
2. Select Catalog: `SampleReports` > `SampleReports.cat`.
3. Select Data Source: `WorldWideSalesBV`. Pick **Region**, **Sales Year**,
   **Total Sales**, **Category**. Studio builds a table.
4. Visualisation toolbar > **Convert or drag to add Crosstab**.
5. Visualisation toolbar > **Crosstab Wizard**. Remove **Sales Year** from the
   **Rows** box and **Category** from the **Columns** box, then add **Category**
   to **Rows**. Confirm the change and Studio rebuilds the crosstab.
6. Visualisation toolbar > **Convert or drag to add Bar**. You now have a bar
   chart of the same data. Other chart types are on the same toolbar.
7. **Save** into **My Reports**.

### Route B: the wizard, and the quarter view

Follows
[Lesson 2: Creating a web report using the wizard](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735498124567-lesson-2-creating-a-web-report-using-the-wizard.md).
This is the route that produces regional sales by quarter with a chart.

1. My Profile > Customize Server Preferences > General: set **Use Wizard for Web
   Report Studio** to **Yes**. Without this the wizard never appears.
2. Resources > **Public Reports** > **SampleReports** > **New** > **Web Report**.
3. Page screen: keep the **Blank** template, label it.
4. Layout screen: pick **T-Style**, and assign **Crosstab**, **Table**, and
   **Banded Object** to the three cells.
5. Bind Data screen, crosstab: data source `WorldWideSalesBV`, **Region** to
   **Columns**, **Sales Month** to **Rows**, **Total Sales** to **Summaries**.
6. Bind the table (details Product Name, Order Date, Total; group by Country) and
   the banded object (details Order ID, Product Name, Quantity, Unit Price, Total;
   group by Country) against the same business view.
7. Style screen: `LogiReportDemo`. **Run**, then **Save** as `.wls`.
8. Now the quarter view: right-click the crosstab row header and choose
   **Switch Row > Sales Quarter**. The row header changes from month to quarter
   without rebuilding anything.
9. Right-click a quarter value > **Go to by Value > Category** to pivot to product
   category within that quarter. **Go Up** and **Go Down** move through the
   business view's hierarchies.
10. Right-click the blank cell at the intersection of the row and column headers >
    **To Chart**. Keep **Clustered Bar 2-D** and map **Total Sales** to **Bar
    Length**, **Category** to **X-Axis**, **Region** to **Clustering**.
11. **Swap Chart Groups** to exchange the category and series axes, then
    **Chart Type > Line > Line 2-D** to change the read from comparison to trend.
12. Right-click the highest node > **Go to Detail** for the rows behind the number.
    Use **Edit Detail Table** first if the default detail fields are not the ones
    you want shown.

**What can go wrong.** Go Up and Go Down do nothing unless the business view has
predefined hierarchies; see
[Track 2: Creating business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519563927-track-2-creating-business-views.md).
Go Down is not the inverse of Go Up: going down applies the currently selected
value as a filter, so you see only that branch. The To Chart dialog offers only the
fields already in the crosstab, so add a measure to the crosstab before converting
if you want it on the chart.

---

## Recipe 2: Pixel-perfect sales report with subtotals and a grand total

The page report answer. Monthly sales broken down by order and month, subtotals per
group, grand total at the end.

Source:
[Lesson 1: Creating a standard banded report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563121559-lesson-1-creating-a-standard-banded-report.md),
component reference
[Working with banded objects](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527064599-working-with-banded-objects.md).

1. Designer > **File > Open Catalog** > `JinfonetGourmetJava.cat`.
2. **File > New > Page Report**, component type **Banded**.
3. Banded Wizard **Data** screen > **\<New Query...\>**, name it, add the tables
   (the lesson uses Orders, Orders Detail, Products), select columns in the Query
   Editor. Auto join is on; inspect the generated SELECT with the SQL button.
4. Work through Display, Group, and Style, then **Finish**.
5. Add summaries to the group footer panels for subtotals and to the banded footer
   for the grand total. See
   [Working with summary fields](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735507390615-working-with-summary-fields.md).
6. **View** tab to preview, **File > Save** as `.cls`.

A banded object is the right shape when the report has repeating detail rows with
calculations attached to a preceding group or to the whole report. That is the
lesson's own framing.

**What can go wrong.** Unused Group Header and Group Footer panels cost
performance; set their **Suppress** property to true. Source:
[Making high-efficiency reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735547328663-making-high-efficiency-reports.md).

---

## Recipe 3: Product sales crosstab, formatted, exported to Excel

Sources:
[Lesson 6: Creating a crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md)
and
[Lesson 4: Creating a chart report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526174871-lesson-4-creating-a-chart-report.md)
for the export step.

1. **File > New > Page Report**, component type **Crosstab**.
2. Data screen > **\<New Query...\>**. The lesson's query joins Customers, Orders,
   Orders Detail, and Products, selecting no columns from Orders because that table
   exists only to carry the joins. Worth saying out loud in a demo: the join table
   need not contribute columns.
3. Display screen: **Category** to Columns, **Customers_Country** to Rows,
   **Quantity** and the **Total** formula to Summaries, then set both Aggregate
   cells to **Sum**.
4. Style screen: **Basic**. **Finish**.
5. Formatting, all through the Report Inspector: set the crosstab **Position** to
   **Absolute** to place it by dragging; add Labels from the Components panel for a
   title and column captions; set **Bold**, **Background**, **Foreground**, and
   **Format** (for example `#,###` and `$#,###.00`) on the cells.
6. If the crosstab splits across pages, clear **Page Layout** on the **View** menu
   tab for continuous mode, then optionally set **Items per Row Block** and **Items
   per Column Block** to 3 to control how much shows at once. Those two properties
   do nothing in pagination mode, and the logic-break documentation scopes them to
   query-based crosstabs, which this recipe is.
7. Right-click the crosstab > **Save Style** to write the formatting to a `.css`
   in `<install_root>\style`, reusable on other crosstabs via **\<Import CSS
   File...\>** on the Home menu tab.
8. **File > Export > To Excel**.

---

## Recipe 4: Parameter-driven date range, then schedule it as a nightly PDF

The recipe that shows governance and delivery rather than pretty pictures.

Sources:
[Lesson 9: Creating a parameter-based report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526219287-lesson-9-creating-a-parameter-based-report.md),
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md),
[Lesson 4: Scheduling reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511111191-lesson-4-scheduling-reports.md).

1. Open an existing page report and **File > Save As** under a new name, so the
   original is untouched.
2. Data panel > **\<New Parameter...\>**: `pStartDate`, Value Type Date, a
   prompting value as the default, prompting text "Please input start date:".
   Repeat for `pEndDate`.
3. Data panel > **Dataset Filter** > **Add Condition**: `ORDER DATE >= @pStartDate`,
   then a second condition for the end date. The two join with And.
4. Preview. Designer prompts for the parameters; **Default** accepts the defaults.
5. Publish the report to Server (**Publish > From Server Machine**, Resource Type
   **Folder with Contents**).
6. On the report row, **Schedule**. General tab: name it. Parameter tab: set the
   values or keep defaults. Publish tab: **To Disk > Publish to Disk > PDF**, path
   `/YourReport.pdf` for the server resource tree. Conditions > Time: **Run this
   task periodically**, Weekly, Sunday, 8:00 PM.
7. **My Tasks** shows it under Scheduled. Hover and **Run** to fire it now rather
   than waiting.

**Why the dataset filter, not the query filter.** A query filter changes the
catalog and therefore every report built on that query. A dataset filter still
pushes down to the database but only affects this report. Stated in the lesson and
in
[Filtering reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534181911-filtering-reports.md).

Add the three-month validation from
[Date type parameter validation](../docs/unversioned/faqs/360052127933-date-type-parameter-validation.md)
if the audience cares about guardrails.

---

## Recipe 5: Shipment detail table with an in-report filter control

Shows an end user filtering a paginated report without leaving it.

Source:
[Lesson 5: Creating a table report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511197847-lesson-5-creating-a-table-report.md).

1. **File > New > Page Report**, component type **Table (Group Above)**.
2. Data screen > new query joining Customers and Orders (auto-joined on customer
   ID).
3. Display screen: add the detail fields, then **Sort Fields By** > Order ID
   ascending.
4. Group screen: **Customers_Territory** first, then **Customer Name**.
5. Style: Classic, vertical. **Finish**.
6. **View > Page Header** to show the page header panel; set the panel **Height**
   to 1.25 in the Report Inspector.
7. **Insert > Web Controls > Drop-down List** into that panel.
8. Right-click the control > **Display Type**. In the Value column, use the
   ellipsis and Insert Fields to bind `Customers_Territory`.
9. In Web Behaviors, Events = **Data Change**, Actions = ellipsis > **\*Filter**.
10. In the Filter Web Action Builder: apply to **TableComp**, Filter On
    `CUSTOMERS_TERRITORY`, Value **Multi-Value Container**. **OK**.
11. Add labels, set **Include Header and Footer** on the Table Comp to false if you
    want to colour the group headers yourself, then style the GH rows.

---

## Recipe 6: Self-service story, business view first

For an audience that asks "can our analysts do this themselves".

Sources:
[Track 2: Creating business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519563927-track-2-creating-business-views.md),
[Business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526420375-business-views.md),
[Track 1: Creating and analyzing ad hoc reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526532375-track-1-creating-and-analyzing-ad-hoc-reports.md),
[Create ad hoc reports](../docs/unversioned/logi-report-get-started-guide/1500009769681-create-ad-hoc-reports.md).

1. In the Catalog Manager, right-click **Business View** under a data source and
   select **New Business View**. Name it.
2. Add tables, let auto join connect them, select the columns you want.
3. In the Business View Editor, create **Categories** as folders (Customers,
   Orders Detail, Products), and drag fields into them. Dragged fields become Group
   objects by default.
4. Change types where needed: select elements, right-click **Edit**, set **Type**
   to **Detail**. Create aggregations with **New View Element**: display name,
   mapping field, Type Aggregation, Aggregate Function Sum. The tutorial builds
   Total Cost, Total Quantity, and Total Sales this way.
5. Rename elements to business language (`Orders_Order ID` becomes `Order ID`).
6. Define hierarchies, for example region down to city, and the product hierarchy.
   These are what make Go Up and Go Down work at runtime.
7. Sort the view elements ascending and **Save**.
8. Now run Recipe 1 on top of it, and the point makes itself: the analyst never
   sees a join.

**Licence note.** The tutorial states this track needs a Live licence for Designer.
Check that before promising it in a proof of concept.

---

## Recipe 7: A dashboard

Build the components as a web report first, test the web report, then save its data
components as library components and assemble them in JDashboard. That is the
documented order, not an optimisation. Sources:
[Report types](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511454487-report-types.md),
[Track 4: Creating library components](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511153047-track-4-creating-library-components.md),
[Track 2: Self-service dashboard with Logi Report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511499671-track-2-self-service-dashboard-with-logi-report.md),
[Create dashboards](../docs/unversioned/logi-report-get-started-guide/1500009742022-create-dashboards.md).

Library components talk to each other through a messaging mechanism, which is what
synchronises data across a dashboard at runtime. Message wiring is documented in
[Delivering messages between library components](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735576827671-delivering-messages-between-library-components.md).

---

## Recipe 8: Subreport inside a report

For "can it show detail from a second query inside the same page". Page reports
only.
[Lesson 8: Creating a report that contains a subreport](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511214359-lesson-8-creating-a-report-that-contains-a-subreport.md),
reference
[Working with subreports](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735521147415-working-with-subreports.md).

---

## Sequencing a full demo

A defensible order, if you have 30 minutes:

1. Recipe 6 briefly, to establish the semantic layer.
2. Recipe 1 live, for interactivity and the conversion moment.
3. Recipe 3 or 2, for pixel-perfect output that the web tools cannot do.
4. Recipe 4, for parameters, scheduling, and delivery.

Rehearse on the shipped sample catalogs first. The corpus documents no sample data
of its own beyond the two catalogs named above, and no scripted demo dataset, so
anything customer-shaped has to be built.

Read [gotchas.md](gotchas.md) before the rehearsal.
