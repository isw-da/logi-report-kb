# Parameters and filters

Two separate mechanisms that a demo usually shows together: a parameter prompts
the user for a value, a filter narrows the data. There are four kinds of filter
and they behave very differently, so pick deliberately.

## The four filter types

From
[Filtering reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534181911-filtering-reports.md):

| Filter | Scope | Pushed to database |
| --- | --- | --- |
| Query filter | every data component using that query, in every report | yes |
| Dataset filter | every component using that dataset, in this report only | yes |
| On-screen filter (filter control) | components sharing the filter control's data source, at runtime | only if Push Down On-screen Filter is set to true (v19) |
| Component filter | one data component in a query-based page report | no |

Query and dataset filters are much more efficient because only filtered data
comes back to the engine. The dataset filter is usually the right choice: it still
pushes down, but it does not change the catalog, so other reports built on the
same query are untouched. The engine may fail to push a filter down for stored
procedures, SOAP web service data sources, and some others.

Component filters are not pushed down. All the data returns and the engine filters
locally, which the documentation calls very inefficient, and they generally cannot
be pushed down even with Push Down Group Query enabled.

The v19 note on pushing down on-screen filters comes with its own caveat: on a
small report, pushing down causes more database round trips and hurts performance.

## Building a component filter

Right-click the data component in a query-based page report, select **Edit
Filter**, then **Add Condition**: field, operator, value. Same procedure and
gotchas from
[Filtering reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534181911-filtering-reports.md):

- Multiple typed values are separated with commas; a literal comma or backslash in
  a value is escaped as `\,` or `\\`.
- On a String field, leaving the value box blank filters on the empty string.
- To catch both spaces and empty strings, build a formula `Trim(@Field)` and filter
  on the formula rather than the field.
- Conditions combine with And, Or, And Not, Or Not, and can be grouped and
  ungrouped, which is the equivalent of parentheses.

## Dataset filters

Data panel > **Dataset Filter**, then **Add Condition**. This is where a parameter
normally lands. Reference:
[Filtering datasets in a report](../docs/logi-report-v17-v19/manipulating-report-datasets-logi-report-designer-v19/5735555312279-filtering-datasets-in-a-report.md).

## Parameters

A parameter is a variable whose value is supplied at runtime, most often to carry
selection criteria into a query or stored procedure. It lives in the catalog
alongside queries, formulas, and summaries. Source:
[Catalogs](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511440151-catalogs.md);
component behaviour in
[Working with parameter fields](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735512482071-working-with-parameter-fields.md).

### Creating one and wiring it up

The tutorial's date-range example, in full, is
[Lesson 9: Creating a parameter-based report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526219287-lesson-9-creating-a-parameter-based-report.md):

1. Data panel > **\<New Parameter...\>** under the Parameters node.
2. Name it (`pStartDate`), keep the default Value Setting, set **Value Type** to
   Date, add a prompting value (the default shown to the user), and write the
   prompting text ("Please input start date:").
3. Repeat for `pEndDate`.
4. Data panel > **Dataset Filter** > **Add Condition**: `ORDER DATE` `>=`, then the
   ellipsis, then double-click `pStartDate` in the Expressions dialog box. Add the
   second condition for the end date; conditions join with And.

The lesson is explicit about why the filter goes on the dataset and not the query:
a query filter applies to every dataset built on that query, so it would also
change the report the tutorial built earlier from the same query.

### At runtime

Designer prompts for parameter values when you preview, with a Default button to
accept the defaults. Server shows an Enter Parameter Values dialog box before
running a parameter-based report, prefilled with any defaults in the template.
Sources: the same lesson and
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md).

Parameter values can also be set per scheduled task, in the Schedule dialog's
**Parameter** tab:
[Specifying parameter values](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741454720023-specifying-parameter-values.md).
A report's default parameter values can be customised on Server with the
**Parameter Settings** command on the resource's floating toolbar.

Why parameters beat post-filtering, in the documentation's own words: they let the
user choose the data before the engine issues the query to the database, so the
query is more efficient.

### Validating a parameter

There is an **On Parameter Value Change** property, on the parameter itself or on
the report template, that runs a formula before any other report action. Used as a
validation rule it returns a message string when the input is wrong and an empty
string when it is fine. The worked example enforces a maximum three-month date
range with `DateDiff("M", @pStartDate, @pEndDate) > 3`. Source:
[Date type parameter validation](../docs/unversioned/faqs/360052127933-date-type-parameter-validation.md).

## Filters at runtime

### Web Report Studio

The **Filter** panel on the left: **Add**, pick fields, and Studio builds a value
list. Selecting a value filters the report and reorders the value list so related
values (for example the countries in the selected region) rise to the top.
**Clear** removes all panel filters. You can also filter a single component
through its wizard on the visualisation toolbar. Sources:
[Lesson 2: Creating a web report using the wizard](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735498124567-lesson-2-creating-a-web-report-using-the-wizard.md)
and
[Applying filters](../docs/unversioned/editing-web-reports-in-web-report-studio/1500009719141-applying-filters.md).
Parameters in Web Report Studio:
[Applying parameters](../docs/unversioned/editing-web-reports-in-web-report-studio/1500009719221-applying-parameters.md).

### Page Report Studio

Business view filters split into predefined filters (defined on the business view
in Designer beforehand) and user-defined filters (created in the studio). They are
set per component, so filtering one component does not affect another component
using the same business view. **Menu > Report > Query Filter**, or right-click the
component and choose **Query Filter**. The dialog has a basic mode for simple
expressions and an advanced mode for grouped conditions with And, Or, And Not,
Or Not. Source:
[Applying filters](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691602-applying-filters.md).

That document states the feature needs a Live licence for Server. It is written in
the Logi JReport era wording, so read the licence name accordingly.

## Web controls: a filter the audience can see

A web control is an object in the report driven by a trigger event and a resulting
web action. The tutorial adds a Drop-down List to a page report's page header,
sets its value to a territory field, sets the event to **Data Change**, and the
action to **\*Filter**, applied to the table on `CUSTOMERS_TERRITORY` with a
Multi-Value Container as the value. The end user then filters the report from the
report itself. Source:
[Lesson 5: Creating a table report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511197847-lesson-5-creating-a-table-report.md);
reference in
[Working with web controls](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735564487575-working-with-web-controls.md)
and, for filter controls specifically,
[Using advanced web controls](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527778327-using-advanced-web-controls.md).

## Era note

The v16 equivalent of the parameter lesson is
[Lesson 9: Creating a parameter-based report](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011463441-lesson-9-creating-a-parameter-based-report.md).
The push-down of on-screen filters is flagged as new in version 19, so do not
promise it against an older deployment.
