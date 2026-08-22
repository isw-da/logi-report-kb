# Quickstart: nothing to a running report

The shortest documented path, in two versions. Both assume Designer and Server
are installed with defaults. Verify the install first with
[Test server installation](../docs/unversioned/logi-report-get-started-guide/1500009769861-test-server-installation.md).

## Path A: fastest to something on screen (web report, no Designer)

This needs a catalog with a business view already published to Server. The
shipped `SampleReports.cat` qualifies. Source:
[Lesson 1: Creating a web report using the quick start method](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519967383-lesson-1-creating-a-web-report-using-the-quick-start-method.md).

1. Start Server. On Windows, `Start Server` in the Logi Report folder on the
   Start menu. Log in with the built-in `admin` / `admin`. Source:
   [Lesson 1: Starting Server](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563057559-lesson-1-starting-server.md).
2. On the Start Page, select **Web Report** in the **Create** category. Web Report
   Studio opens in a new tab.
3. In Select Catalog, pick the catalog (for example `SampleReports` >
   `SampleReports.cat`).
4. In Select Data Source, pick a business view, then pick the view elements you
   want. Studio builds a table from them.
5. Use the vertical visualisation toolbar to convert the table to a crosstab, or
   to a bar chart, in one click.
6. **Save**, choose a folder such as **My Reports**, name it.

That is a working, saved, interactive report without opening Designer.

## Path B: the real build (page report from a query, in Designer)

Source:
[Lesson 1: Creating a standard banded report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563121559-lesson-1-creating-a-standard-banded-report.md),
with the connection steps from
[Connections](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735506277911-connections.md).

1. Open Designer. On the Start Page choose your database under **Connect** (SQL
   Server, Oracle, MySQL, InterSystems IRIS, and PostgreSQL have plug-ins; anything
   else needs its JDBC driver installed and added to Designer's environment
   configuration file first).
2. Choose **New Catalog**, name it, then supply server, database, user, password.
   **Test Connection** before continuing.
3. Designer opens the Catalog Manager. Select **Add Tables**, choose the database
   catalog and schema, **Refresh**, select tables, **Add**, then **Done**. Rename
   tables to something meaningful by right-clicking and selecting **Rename**.
4. **File > New > Page Report**. Choose a starting component: Banded, Table (Group
   Above), Table (Group Left), Table (Group Left Above), Summary Table, Chart,
   Crosstab, Horizontal Banded, Mailing Label, Tabular, or Blank. The full list is
   in [Start creating new reports](../docs/unversioned/logi-report-get-started-guide/1500009742142-start-creating-new-reports.md).
5. In the wizard's **Data** screen, select **\<New Query...\>**, name it, add the
   tables you need, then pick columns in the Query Editor. Auto join is on by
   default, and Designer builds the SELECT for you.
6. Work through the wizard's remaining screens: Display (fields), Group, Style.
   **Finish**.
7. Select the **View** tab to preview against real data. See
   [Previewing reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735555715607-previewing-reports.md).
8. **File > Save** as a `.cls` file.

## Getting it onto Server

You must publish a report together with its catalog the first time. After that
you can publish report updates alone, as long as the catalog stays published and
unchanged. Source:
[Lesson 2: Publishing resources](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511100055-lesson-2-publishing-resources.md).

1. Server Console > **Resources** > open **Public Reports**.
2. **Publish > From Server Machine** on the task bar.
3. Leave Resource Type as **Folder with Contents**, browse to the folder holding
   the catalog and reports, give it a Resource Node Name and description, **OK**.

Then run it: select the report link to run in the default format, or hover the
row and use **Advanced Run** to pick a format (HTML, PDF, Text, Excel, PostScript,
RTF, XML). Source:
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md).

## If you just need something to point at

Server ships sample reports and sample catalogs. See
[View sample reports](../docs/unversioned/logi-report-get-started-guide/1500009769901-view-sample-reports.md)
and
[Open sample report templates](../docs/unversioned/logi-report-get-started-guide/1500009769821-open-sample-report-templates.md).
The tutorial's own catalog, `JinfonetGourmetJava.cat`, sits under
`<install_root>\Demo\Reports\JinfonetGourmetJava`, with finished versions of every
tutorial report in `<install_root>\Demo\Reports\TutorialReports`.

Next: [concepts.md](concepts.md) if the catalog chain is unclear,
[demo-recipes.md](demo-recipes.md) for end-to-end walkthroughs.
