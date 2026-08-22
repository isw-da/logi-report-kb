---
title: "Working with Components in Reports"
id: 45190430701069
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190430701069-Working-with-Components-in-Reports
updated_at: 2026-04-30T15:12:03Z
source_host: logi-report-v26.insightsoftware.com
---
# Working with Components in Reports

Components are the objects that you can place in reports. Report provides a full set of components that enable you to present and control the report data and presentation in a wide variety of ways. This topic introduces  the usage of each component. It also briefly describes how Report classifies the components and what data components are.

You can use the following components in Report:

- Chart

- Table

- Crosstab

- Banded Object

- Map

- KPI

- Label

- DBField

- Parameter Field

- Summary Field

- Formula Field

- Special Field

- Tabular

- Web Control

- Image

- Multimedia Object

- Text Box

- Subreport

- Drawing Object

- UDO

- Barcode

- Rank

See Component Placement in Different Report Type about the components you can use in different report types, and the report areas where you can place them in a report.

## Component Categories

Report classifies the components into the following categories:

- 
Visual: Chart, Map, KPI, and Rank 

- 
Grid: Table, Crosstab, and Tabular

- 
Basic: Label, Text Box, Image, Subreport, and Banded Object

- 
Data Field: DBField, Formula Field, Summary Field, and Parameter Field

- 
Web Control: Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, and Form

- 
Special Field: Print Date, Print Time, Fetch Date, Fetch Time, Record Number, and many more

- 
Drawing Object: Line, Arc, Box, Oval, and Round Box

- 
Multimedia Object: Applet, RealMedia, and Windows Media

- 
Others: UDO and Barcode

 

## 
Data Components

Some components must be bound with a dataset to display data, so Report refers to them  as data components or data containers. These components include Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI. In page reports and web reports, when two data containers in a parent-child relationship apply different datasets, you can use data container links to set up data relations between them.

 After you bind a dataset to the report body, Report also regards the report body as a special data container. In this case, if you place a tabular directly inside the report body, the tabular applies the same dataset as the report body and becomes a data container too; if you place nested tabulars and the parent of the outermost tabular is the report body, all these tabulars apply dataset of the report body and turn to be data containers.
