---
title: "Specifying Parameter Values"
id: 28898366963597
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898366963597-Specifying-Parameter-Values
updated_at: 2026-02-26T02:11:07Z
source_host: docs-report.zendesk.com
---
# 
Specifying Parameter Values 

You need to specify the parameter values when you run or schedule a report via API, and if the report contains parameters. This topic describes how you can specify  values to Multi-valued Parameters and specify dynamic parameter values. 

This topic contains the following sections:

- Setting Values of Multi-valued Parameters

- Setting Dynamic Parameter Values

## 
Setting Values of Multi-valued Parameters

Take the following example to set values to a multi-valued parameter Customers_Country: 

String[] a = {"USA", "Canada"}; 
  props.put(APIConst.TAG_PARAM_PREFIX + "Customers_Country", a);

If you want the parameter to use all its values, take the following: 

props.put(APIConst.TAG_PARAM_PREFIX + "Customers_Country",
 new String[]{APIConst.MULTIPLE_ALL_VALUE});

For the API code of running a report, see APIDemoRunReport.java in  <install_root>\help\samples\APIServer.

## 
Setting Dynamic Parameter Values

You can specify dynamic parameter values by implementing the ParameterGenerator interface.

To set dynamic parameter values to a report:

- Create a class MyParameterGeneratorImpl to implement the ParameterGenerator interface. See the API demo DemoParameterGenerator.java in  <install_root>\help\samples\APIParameter for an example of implementing the ParameterGenerator interface.

- Add the class path into the class path of your implementation of running or scheduling the report such as DemoParameterRunReport.

- In DemoParameterRunReport, replace the way of setting static parameter values and instead set dynamic values of the parameters you want in the report. Take the parameter PToday for example:
    First disable or delete the line:

props.put(APIConst.TAG_PARAM_PREFIX + "PToday", "2007-5-21");

and then add a line: 

props.put(APIConst.TAG_PARAM_PREFIX + "PToday", APIConst.TAG_PARAM_GEN_PREFIX + "MyParameterGeneratorImpl";
