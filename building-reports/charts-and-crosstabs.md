# Charts and crosstabs

The two components a demo almost always needs. Both are built through a wizard,
and the wizard's screens differ depending on whether the data resource is a query
or a business view.

## Charts

### How a chart holds data

A chart (Stock aside) shows one, two, or three dimensions, one per axis: category
axis, series axis, value axis. The field on the series axis always holds a higher
group level (the outer group) than the field on the category axis. Two-dimensional
charts have no series axis. The value-axis field must be numeric. Source:
[How data is represented in a chart](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735511926551-how-data-is-represented-in-a-chart.md).

Three shapes of chart, from that same document:

- detail records only, two or three dimensions;
- summaries only, one dimension, used to compare several summary fields;
- detail plus summary, the most common form.

Two warnings the document gives outright: if a chart takes a long time to run and
shows many duplicate categories, rebuild it on summaries; and three-dimensional
charts are hard to read, so prefer a clustered bar over a 3-D bar. Take both into
a demo.

For the value axis to carry more than one field, the fields must be at the same
level, meaning all DBFields or formulas of the dataset for a two-dimensional
chart, or summaries of the same group level for a three-dimensional one. And it
cannot carry more than one field at all when the chart uses a 3-D subtype or any
subtype of Pie, Radar, Gauge, or Surface. Dropping a second measure onto a pie or a
gauge in a demo will not work.

A combo chart has two value axes, primary and secondary, each carrying one or
more subtypes. The most common combo is a bar on the primary axis and a line on
the secondary.

### Chart types

More than ten general types, most with subtypes: Bar, Bench, Line, Area, Pie and
Donut, Radar, Organisation, Indicator, Gauge (Dial, Solid, Activity, Bar,
Bubble), Surface, Scatter, Bubble, Stock (High-Low, High-Low-Close,
Open-High-Low-Close), Bullet, Heat Map, and Combo. The full table with what each
is for is
[Chart types](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527491351-chart-types.md).

Bullet is documented as the replacement for the meters and gauges that dashboards
usually reach for, on the grounds that its linear design reads more efficiently
than a radial meter. Useful line in a demo.

### Building one

Insert routes and the full wizard walk-through are in
[Inserting charts in a report](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735512245143-inserting-charts-in-a-report.md);
the component overview is
[Working with charts](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735563831831-working-with-charts.md).

The worked tutorial example, a clustered bar of annual sales by region, runs
Data > Type > Display > Layout > Style:

1. **Data**: pick the query or business view.
2. **Type**: pick the chart type, for example Clustered Bar 2-D.
3. **Display**: drag a field to **X-Axis**, a field to **Clustering** (the series),
   and a numeric field or summary to **Bar Length**. You can create a new formula
   or a new summary from inside this screen; the tutorial builds a Sum summary
   grouped by the X-axis formula.
4. **Layout**: chart title, category axis title, and options to hide elements such
   as the legend and wall.
5. **Style**: apply a CSS style such as Classic.

Source:
[Lesson 4: Creating a chart report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526174871-lesson-4-creating-a-chart-report.md).

### Formatting

Every chart part has its own format dialog box: double-click a bar for Format Bar
(depth, subtype, data labels), right-click the legend for Format Legend (font,
mark shapes per item), right-click and use Format Axes > Format Value (Y) Axis for
number formats such as `$#,##0`. Data labels can be static, positioned on the
chart, or dynamic, appearing on hover. See
[Modifying charts](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735498861207-modifying-charts.md)
and the same tutorial lesson.

## Crosstabs

### Building one

The wizard's Display screen has three boxes: **Columns**, **Rows**, and
**Summaries**. Source:
[Inserting crosstabs in a report](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527515799-inserting-crosstabs-in-a-report.md).

On a business view, Columns and Rows take group objects (or dynamic formulas used
as Group), and Summaries takes aggregation objects, detail objects, or dynamic
aggregations. When you put a detail object into Summaries you must set its
aggregate function yourself in the **Aggregate** cell.

The per-field controls differ by box. On Columns and Rows fields: **Label** (blank
by default, so no header label shows unless you set one or tick Auto Map Field
Name), **Color**, **Sort** (Ascend, Descend, No Sort), **Move Up** and **Move
Down** for display order, and **Remove**. On Summaries fields: **Aggregate** (with
**Distinct On** when you pick DistinctSum), **Label**, **Comparison Function**,
Move Up and Move Down, and Remove. Colour and sort are not offered on summaries.

The tutorial's query-based version drags Category to Columns, Country to Rows, and
Quantity plus a Total formula to Summaries, then sets both aggregates to Sum:
[Lesson 6: Creating a crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md).

### Crosstab page layout

A crosstab in pagination mode often splits across pages, which ruins the read. The
documented fix is continuous mode: clear **Page Layout** on the **View** menu tab
and Designer lays the whole report out on a single page. Source:
[Lesson 6: Creating a crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md).

In continuous mode you can further limit how many items show at a time with the
crosstab's **Items per Row Block** and **Items per Column Block** properties. Two
constraints: they have no effect in pagination mode, and the logic-break document
scopes these four crosstab properties (Current Row Block Index, Current Column
Block Index, Items per Row Block, Items per Column Block) to a **query-based**
crosstab. The corpus does not document an equivalent for a business-view crosstab.
Source:
[Designing the report pages](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735569908631-designing-the-report-pages.md).

### Beyond the basics

[Modifying crosstabs](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527527447-modifying-crosstabs.md)
covers comparison functions and structural edits;
[Using crosstab formulas](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735520960151-using-crosstab-formulas.md)
covers calculated cells;
[Working with crosstabs](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735498924183-working-with-crosstabs.md)
is the overview.

## The conversion trick, which is the demo

In Web Report Studio the vertical visualisation toolbar converts a data component
between table, crosstab, and chart in one click, and the same toolbar gives you
the component's wizard for redefining fields or applying a filter. Right-clicking
the blank cell at the intersection of a crosstab's row and column headers gives
**To Chart**, which opens a dialog listing only the fields already in the crosstab
and lets you map them to Bar Length, X-Axis, and Clustering. Sources:
[Lesson 1: Creating a web report using the quick start method](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519967383-lesson-1-creating-a-web-report-using-the-quick-start-method.md)
and
[Lesson 2: Creating a web report using the wizard](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735498124567-lesson-2-creating-a-web-report-using-the-wizard.md).

On a chart in Web Report Studio: **Swap Chart Groups** exchanges the category and
series axes, **Chart Type** changes the type live, hovering a node shows its
value, and right-click gives **Go to Detail** with **Edit Detail Table** to choose
which fields the detail table shows. On a crosstab: **Switch Row**, **Go to by
Value**, **Go Up**, and **Go Down**, where go up and go down need hierarchies
predefined in the business view.

The single-click versions of these are documented separately as
[One-select ad hoc operations](../docs/unversioned/one-select-ad-hoc-operations/1500009778981-one-select-ad-hoc-operations.md),
including
[One select to convert table, crosstab, chart](../docs/unversioned/one-select-ad-hoc-operations/1500009750442-one-select-to-convert-table-crosstab-chart.md)
and
[One select to pivot crosstab](../docs/unversioned/one-select-ad-hoc-operations/1500009779001-one-select-to-pivot-crosstab.md).

## Two constraints that bite

- A page report's data resource type is fixed when you create the report, by the
  **Create Using Business View** option. Every data component in that page report
  must then use the chosen type. You cannot mix a query-based chart with a
  business-view-based crosstab in one page report. Source:
  [Inserting crosstabs in a report](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527515799-inserting-crosstabs-in-a-report.md).
- Business-view-based page reports and web reports allow 2-D charts only. Source:
  [Component placement in different report type](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/9898540172311-component-placement-in-different-report-type.md).
  That same document shows charts are not allowed in the banded page header,
  detail, or page footer panels of a page report, but are allowed in banded group
  header and group footer panels, which is exactly where you put a chart that
  should repeat per group.

## Era note

The Logi JReport era has the equivalent lessons:
[Lesson 4: Creating a chart report](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011431402-lesson-4-creating-a-chart-report.md)
and
[Lesson 6: Creating a crosstab report](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011431382-lesson-6-creating-a-crosstab-report.md).
The v17 to v19 chart type list is the one to quote, since heat map, bullet, and
the gauge subtypes are documented there.

The unversioned property references for these components sit at
[Chart](../docs/unversioned/chart/1500009718301-chart.md),
[Chart legend](../docs/unversioned/chart/1500009692022-chart-legend.md), and
[Table](../docs/unversioned/table/1500009692302-table.md).
