---
title: "Component Placement in Different Report Type"
id: 28897842236941
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897842236941-Component-Placement-in-Different-Report-Type
updated_at: 2024-09-30T09:09:46Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Component Placement in Different Report Type

The components you can use vary by the report type: page report (query-based or business view-based), web report, or library component. In a report, you can place components  within banded objects or some other components, in the page headers and footers, and in an empty area in the report body. When you insert a component, Designer indicates whether the target location is valid for the component. This topic describes the components you can use in different report types, and uses tables to show the report areas in each report type that are valid locations for different components.

- Components in Query-Based Page Report

- Components in Business View-Based Page Report

- Components in Web Report

- Components in Library Component

 The following tables show whether you can place a component type in different report areas generally. You may find Designer does not allow adding some specific components of a type to a location. For example, you see "Y" for Web Control in all the banded panel columns in the page report tables, but you can insert the Expand/Collapse Group web control in Banded Page Header Panel (BPH) only.

## 
Components in Query-Based Page Report

As Designer indicates in the Insert ribbon, you can use all components except KPI in page reports that apply query resources.

|  | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | Text Box | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBField | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Formula Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Summary Field | N | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N |
| Parameter Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Label | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Text Box | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| Image | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Table | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| Crosstab | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| Chart | Y | Y | N | N | N | Y | Y | Y | N | Y | N | Y |
| Tabular | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| Banded Object | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| Subreport | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| UDO | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N |
| Map | Y | Y | N | N | N | Y | Y | Y | N | Y | N | Y |
| Special Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Drawing Object | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N |
| Web Control | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Multimedia Object | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y |
| Barcode | You can insert barcode and rank components in a report area that is valid for the component on which the barcode or rank is based. For example, you can insert a rank component that represents a DBField in the report areas in which a DBField component is allowed. |  |  |  |  |  |  |  |  |  |  |  |
| Rank |  |  |  |  |  |  |  |  |  |  |  |  |

## 
Components in Business View-Based Page Report

You can use the following components in business view-based page reports: DBField, Formula Field, Summary Field, Parameter Field, Label, Text Box,  Image,  Table, Crosstab, 2-D Chart, Banded Object, Subreport, Special Field, Drawing Object, Web Control (advanced web controls and Form only), and Multimedia Object.

|  | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Text Box | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBField | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Formula Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Summary Field | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| Parameter Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Label | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Text Box | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| Image | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Table | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| Crosstab | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| Chart | Y | Y | N | N | N | Y | Y | Y | N | N | Y |
| Banded Object | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| Subreport | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| Special Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Drawing Object | N | Y | Y | Y | Y | Y | Y | Y | N | N | N |
| Web Control | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Multimedia Object | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y |

## 
Components in Web Report

You can use the following components in web reports: DBField, Formula Field, Summary Field, Parameter Field, Label, Text Box, Image, Table, Crosstab, 2-D Chart, Banded Object, KPI, Tabular, Map (Geographic Map only), Special Field, Drawing Object (Line only), Web Control (excluding Expand/Collapse Group and Form), and Multimedia Object.

|  | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | Text Box | KPI | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBField | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| Formula Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| Summary Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| Parameter Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N |
| Label | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Text Box | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| Image | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Table | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| Crosstab | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| Chart | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| KPI | N | N | N | N | N | N | N | N | Y | N | N | Y |
| Tabular | N | N | N | N | N | N | N | N | N | N | N | N |
| Banded Object | N | N | N | N | N | N | N | N | Y | N | N | Y |
| Geographic Map | N | N | N | N | N | N | N | N | Y | N | N | Y |
| Special Field | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | N |
| Drawing Object | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | N |
| Web Control | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| Multimedia Object | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | N | Y |

## 
Components in Library Component

You can use the following components in library components: DBField, Formula Field, Summary Field, Parameter Field, Label, Image, Table, Crosstab, 2-D Chart, KPI, Map (Geographic Map only), Special Field, and Web Control (excluding Expand/Collapse Group and Form).

|  | Body | Table Cell | KPI |
| --- | --- | --- | --- |
| DBField | Y | Y | Y |
| Formula Field | Y | Y | Y |
| Summary Field | Y | Y | Y |
| Parameter Field | Y | Y | N |
| Label | Y | Y | Y |
| Image | Y | Y | Y |
| Table | Y | N | N |
| Crosstab | Y | N | N |
| Chart | Y | N | N |
| KPI | Y | N | N |
| Geographic Map | Y | N | N |
| Special Field | Y | Y | N |
| Web Control | Y | N | N |

Previous Topic  Next Topic
