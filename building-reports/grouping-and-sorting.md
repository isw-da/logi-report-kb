# Grouping and sorting

Grouping happens at design time in the component wizard, and again at runtime in
the studios. Sorting is separate from grouping, and there are two different things
called sorting.

## Grouping at design time

For a table, the wizard's **Group** screen (called **Columns** for a summary table
in a web report or library component) adds group levels. In a page report you can
also use **Insert > Group**. Full procedure:
[Grouping data in tables](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527697943-grouping-data-in-tables.md).

- On a business view, the group-by field must be a group object, or a dynamic
  formula used as Group.
- On a query resource, it can be a DBField, or a formula or parameter valid to
  those DBFields in the catalog.
- Order the levels with Move Up and Move Down. Designer then renders a GH and GF
  (group header and group footer) row pair per level.

You cannot group these SQL types: `SQL_BINARY`, `SQL_BLOB`, `SQL_CLOB`,
`SQL_LONGVARCHAR`, `SQL_LONGVARBINARY`, `SQL_VARBINARY`, `SQL_OTHER`.

The tutorial's two-level example groups a shipment table by Territory then by
Customer Name:
[Lesson 5: Creating a table report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511197847-lesson-5-creating-a-table-report.md).
For a banded object the group structure is the same idea in panels rather than
rows; see
[Working with banded objects](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527064599-working-with-banded-objects.md)
and
[Lesson 1: Creating a standard banded report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563121559-lesson-1-creating-a-standard-banded-report.md).

## Sorting groups versus sorting records

These are different operations with different scopes, and the distinction is
stated plainly in
[Sorting report data](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691702-sorting-report-data.md):

- Sorting records changes the order of records across the whole banded object or
  table, or within each group if groups exist. Scope: the whole component.
- Sorting groups at a group level changes the order of the groups at that level,
  by the value of the first record in each group on the chosen field. Scope: that
  group level.

You cannot sort by a global level formula.

### Group sort options

Set per group level in the **Sort** column of the Group screen. Options, from
[Grouping data in tables](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527697943-grouping-data-in-tables.md):

| Option | Effect |
| --- | --- |
| Ascend | groups in ascending order |
| Descend | groups in descending order |
| No Sort | groups in their original order |
| Special Group | query resources only; opens User Defined Group for custom grouping rules |
| Custom Sort | sort groups by other fields, using the first record in each group |

### Record sort at design time

The table wizard's Display screen has **Sort Fields By**, where you add sort-by
fields. The tutorial sorts a shipment table by Order ID ascending there. By
default Designer displays records in the order the fetch returns them.

### Sorting at runtime

In Page Report Studio, **Menu > Report > Sort** or the Sort toolbar button opens
the Sort dialog: pick a scope (the component, or a group field), pick a field, pick
Ascend or Descend. You can add further rows and reorder them to set sort priority
only when the scope is the banded object or table; with a group field selected only
one sort condition can be composed. Right-clicking a value
also gives **Sort > Ascend / Descend / No Sort**, where right-clicking a detail or
summary value affects records and right-clicking a group value affects that group
level. A shortcut-menu sort replaces the previous shortcut-menu sort rather than
adding to it.

In Web Report Studio, hovering a column header shows sort arrows; the tutorial
sorts Order Date descending that way. Source:
[Lesson 2: Creating a web report using the wizard](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735498124567-lesson-2-creating-a-web-report-using-the-wizard.md).
The one-click version is
[One select to sort and filter table](../docs/unversioned/one-select-ad-hoc-operations/1500009750482-one-select-to-sort-and-filter-table.md).

## Select N: top and bottom

Two independent Select N settings, both in the Group screen:

- Select the **Table** node, then **Select N**, to keep only the first or last N
  records in the whole table.
- Select a group-by field, then **Select N**, to keep only the first or last N
  groups at that level. Tick **Other** and name it to collect the remaining groups
  into an extra group instead of hiding them.

They are not mutually exclusive. You can drive N from an Integer parameter, but
that parameter needs a default value greater than zero or users get an exception at
runtime. Source:
[Grouping data in tables](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527697943-grouping-data-in-tables.md).

## Grouping by intervals

When a group-by field is Numeric, String, or Date/Time, the **Special Function**
column groups by intervals rather than by exact value, for example "Up to 5",
"Up to 10", "Up to 50" for numeric fields. This is only available in page reports
that use query resources. Same source.

## Summaries and aggregation

A summary is a built-in aggregate (Count, Average, Sum, standard deviation and
others) defined against a group. In the Designer wizards you create one with
**\<New Summary...\>**: choose the aggregate function, the field to summarise, and
the Group By field. Sources:
[Catalogs](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511440151-catalogs.md)
and
[Working with summary fields](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735507390615-working-with-summary-fields.md).

At runtime in Web Report Studio, right-click a value in a numeric column and
choose **Aggregate On**, pick Sum, and the total appears in each group header.
That also creates a dynamic aggregation (named `Sum_<field>` by default) which
then appears under Dynamic Resources > Aggregations in the Resources panel and can
be reused. Source: the web report wizard lesson above.

Ranking is a separate component:
[Working with ranks](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735564383767-working-with-ranks.md).

## Adding a group at runtime

In Web Report Studio you can drag a field from the Resources panel above an
existing group in a table and drop when the orange line appears, which adds a
group level. In a banded object you open **Edit Template** on the visualisation
toolbar and drag the field onto the GH panel. Right-clicking a group value gives
**Switch Group** to change which field the level groups by. Source: the web report
wizard lesson.

## Era note

The Page Report Studio sorting document sits in `docs/unversioned/` and names the
product Logi JReport Designer in one tip, so read it as the older text; the
behaviour it describes is unchanged in the v17 to v19 designer documents. Group
filters, Select N, and interval grouping are documented in the v17 to v19 set.
