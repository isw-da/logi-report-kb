# Scheduling, export, and delivery

Three separate things that a demo tends to blur: exporting from Designer, running
a report on demand from Server in a chosen format, and scheduling a task that
publishes results to a destination.

## Export formats

A page or web report can be exported to: Logi Report Result, HTML, PDF, Excel,
Text, RTF, XML, PostScript, Mail, and Fax. Source:
[Exporting reports](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735544904599-exporting-reports.md).

Per-format detail:
[PDF](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531895447-exporting-reports-to-pdf.md),
[Excel](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735516034199-exporting-reports-to-excel.md),
[HTML](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735553350295-exporting-reports-to-html.md),
[Text](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735525405719-exporting-reports-to-text.md),
[RTF](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531933591-exporting-reports-to-rtf.md),
[XML](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735516111511-exporting-reports-to-xml.md),
[PostScript](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531904791-exporting-reports-to-postscript.md),
[Mail](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531881623-exporting-reports-to-mail.md),
[Fax](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735553344535-exporting-reports-to-fax.md),
[Logi Report Result](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735525374615-exporting-reports-to-logi-report-result.md),
[Accessible HTML and PDF](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735567902231-exporting-reports-to-accessible-html-and-pdf.md),
and
[Printing reports](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531983767-printing-reports.md).

Advanced Run on Server offers a narrower set: HTML, PDF, Text, Excel, PostScript,
RTF, and XML. Source:
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md).

### Exporting from Designer

**File > Export > To PDF** (or the format you want). If you have modified the
report since opening it, switch to the **View** tab and select **Refresh Data**
first, so the engine refetches from the database; otherwise export from either
design or view mode. Source:
[Exporting reports](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735544904599-exporting-reports.md).

### Page settings and layout precision

**File > Page Setup > Export** tab, choose the format from **Export To**, and set
page settings per format. Pagination mode is the default; clearing **Page Layout**
gives continuous mode, so the output lands on a single page. Server applies these
same settings when users advanced-run or schedule the report in that format.

**File > Options > Export to > Layout Precision** sets High or Low precision. The
default is "Optimize for speed over visual effect". High precision gives better
layout and slower export; by default PDF, RTF, Excel, Fax and PostScript export
text at high precision, while HTML, Logi Report Result, XML, and Text do not. For
page reports, custom precision only takes effect on report tabs whose **Precision
Sensitive** property is true.

### PDF worth knowing for a demo

From
[Exporting reports to PDF](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531895447-exporting-reports-to-pdf.md):
select which report tabs to export and in what order; **TOC** includes the report's
TOC tree; **Accessible PDF** for accessibility; **Encrypt** for open and permission
passwords with Acrobat 3.0 (40-bit RC4) or Acrobat 5.0 (128-bit RC4) compatibility,
printing and editing permissions, and a screen-reader access option; **Sign** for a
digital signature. Charts, barcodes, web controls and UDOs export as images
(recommended) or vector graphics. **Run Linked Report** generates linked reports
too and is called out as a performance risk on large data.

`Drilldown` in PDF only works on page reports using query resources, with grouped
banded objects and summaries added to the groups, and only if those summaries are
neither hidden nor suppressed.

## Exporting from the studios

Web Report Studio: **Menu > File > Export**, or the Export button. Formats HTML,
PDF, Text, Excel, RTF, XML, PostScript. Destination choices are **View Report
Result** (opens in the browser), **Save to File System**, or **Save to Version
System** (a result version in Server's versioning system). You can also apply a
style group on the way out. Printing offers a real printer, or **Save as PDF** or
**Save as HTML** to print locally. Source:
[Exporting/printing the report result](../docs/unversioned/editing-web-reports-in-web-report-studio/1500009692782-exporting-printing-the-report-result.md).

Page Report Studio's equivalent:
[Exporting/printing the report result](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009718161-exporting-printing-the-report-result.md).

## Running on demand versus scheduling

Running a report on demand makes the user wait, and Server does not save the
result in the versioning system unless the user explicitly saves it. Scheduling
runs the report in the background, so the user carries on working, other
interactive users are not affected, and Server keeps the result in the versioning
system. That is the argument the tutorial makes for scheduling even a task you
want to run immediately. Source:
[Lesson 4: Scheduling reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511111191-lesson-4-scheduling-reports.md).

## Scheduling: the six destinations

Versioning System, File System (To Disk), Email, Printer, Fax, and FTP. Sources:
the same lesson and
[Scheduling to run a report](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741463322647-scheduling-to-run-a-report.md).
To Disk is unavailable to organisation users under multitenancy.

### The Schedule dialog, tab by tab

- **General**: schedule name; for a page report, which report tabs to run, with
  **Export to One File** if several tabs should land in one output; dynamic
  connection; report and catalog version; priority (administrators only, ignored
  unless `server.properties` sets `queue.policy` to something other than 0);
  Advanced settings for style group, encoding, NLS language, DB user and password,
  TaskListener, preferred cluster server, and **Enable Auto Recover Task** with a
  retry count and interval.
- **Parameter**: set values, or keep the defaults.
- **Publish**: pick the destinations and the format for each.
- **Conditions > Time**: **Run this task immediately**, **Run this task at** a
  specified time, or **Run this task periodically** with duration, date and time,
  plus exception dates on which not to run. Set the time zone here.
- **Notification**: email notifications on success or failure.

### Three worked examples

From
[Lesson 4: Scheduling reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511111191-lesson-4-scheduling-reports.md),
and expanded in
[Examples of scheduling reports](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741483494551-examples-of-scheduling-reports.md):

1. **To Version**: Publish tab > To Version > Publish to Versioning System, choose
   Page Report Result format, tick **Result Auto-delete** and set **Result Expires
   in 7 Days**. Run immediately. View the output later with the **Version** command
   on the report's floating toolbar.
2. **To Disk**: Publish > To Disk > Publish to Disk > PDF. Keeping **Publish to
   Server Resource Tree** and typing `/CustomerContactCard.pdf` writes into the
   server disk path, `<install_root>\jreports` by default, so the path must start
   with `/`. A full path such as `C:\temp\CustomerContactCard.pdf` writes outside
   the resource tree. Schedule weekly, Sunday, 8:00 PM.
3. **To Printer**: Publish > To Printer > Publish to Printer, then a monthly time
   condition such as the 1st day of every 2 months at 7:00 AM.

Monitor everything on **My Tasks**: Running, Completed, and Scheduled tables. You
can force a scheduled task to run now with **Run** on its floating toolbar.

### Related scheduling topics

[Scheduling reports](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741483442455-scheduling-reports.md),
[Scheduling to run multiple reports](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741454859671-scheduling-to-run-multiple-reports.md),
[Scheduling bursting reports](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741463244055-scheduling-bursting-reports.md),
[Viewing scheduled reports](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741469840663-viewing-scheduled-reports.md),
[Applying dynamic names for published report files](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741483587607-applying-dynamic-names-for-published-report-files.md),
and
[Importing and exporting scheduled tasks](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741483570071-importing-and-exporting-scheduled-tasks.md).

Bursting is the feature that splits one run into per-recipient outputs; the design
side is
[Creating bursting reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534125591-creating-bursting-reports.md).
It is a page report feature only.

## Publishing

Publishing is the prerequisite for all of the above: Server can only run what has
been published to it, and a report must be published together with its catalog the
first time.
[Lesson 2: Publishing resources](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511100055-lesson-2-publishing-resources.md)
covers the Server Console route,
[Publishing and downloading resources](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735576653207-publishing-and-downloading-resources.md)
the Designer route.

## Era note

[Scheduling to run a report](../docs/unversioned/scheduling-tasks-to-run-reports/1500009778481-scheduling-to-run-a-report.md)
in the unversioned set lists the same six task types. The unversioned
[Scheduling reports](../docs/unversioned/scheduling-reports/1500009749542-scheduling-reports.md)
is a section overview and does not enumerate destinations, so do not cite it for
the list. The v16 lesson is
[Lesson 4: Scheduling reports](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011463561-lesson-4-scheduling-reports.md).
The v19 additions worth not over-promising on older builds: custom file extensions
on export, PDF Title and Subject properties, and per-format continuous mode in
Page Setup, all marked new for version 19 or 19.2 in the source.
