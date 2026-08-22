---
title: "JDashboard Basic Concepts"
id: 45203874124557
section: "Introduction to the JDashboard and Visual Analysis Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203874124557-JDashboard-Basic-Concepts
updated_at: 2026-04-30T14:08:05Z
source_host: logi-report-v26.insightsoftware.com
---
# 
JDashboard Basic Concepts 

This topic describes the main JDashboard concepts: library components, component library, and dashboards.

Library components

You can use library components and data components in reports to build dashboards. They can present data via intuitive components such as charts, crosstabs, tables, KPIs, and geographic maps. You can create and edit library components using Report Designer, and then publish them to Report Server for use in dashboards. Library components can also come from report components. You can save a data component in a web report to a library component, using either Web Report Studio or Report Designer. Library components use .lc as the file suffix. 

Component library

Component library contains one Public Components folder and a My Components folder for each specific dashboard user. 

Public Components and My Components are two built-in folders in the server resource tree root for storing library components. The Public Components folder contains public components available to everyone. The My Components folder holds personal components for each dashboard user.

Dashboard

A workspace window that can contain any number of library components.

- 
Components from library
    When inserting a library component from the component library into a dashboard, you are not copying the component from the library, but instead referencing it from the library.

- 
Report components
 You can insert data components, such as tables, charts, crosstabs, KPIs, and geographic maps in reports, into dashboards as library components.

- 
Objects from the Toolbox
    In addition to library components, you can select objects from the Toolbox such as labels, images, special fields, filter controls, third-party objects, and HTML components.
