---
title: "Specifying Parameter Values"
id: 1500009712121
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712121-Specifying-Parameter-Values
updated_at: 2021-11-03T06:58:32Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686282-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712221-Specifying-Report-Running-Properties-in-the-Session)

# Specifying Parameter Values

When you run or schedule a report via API, if the report contains parameters, you need to specify the parameter values. This topic is about setting parameter values.

Below is a list of the sections covered in this topic:

* [Setting Values of Multi-value Parameters](#Multi)
* [Setting Dynamic Parameter Values](#Dynamic)

## Setting Values of Multi-value Parameters

Take the following example to set values to a multi-value parameter Customers\_Country:

`String[] a = {"USA", "Canada"};   
 props.put(APIConst.TAG_PARAM_PREFIX + "Customers_Country", a);`

If you want the parameter to use all its values, take the following:

`props.put(APIConst.TAG_PARAM_PREFIX + "Customers_Country",
new String[]{APIConst.MULTIPLE_ALL_VALUE});`

For the API code of running a report, see APIDemoRunReport.java in  `<install_root>\help\samples\APIServer`.

## Setting Dynamic Parameter Values

You can specify dynamic parameter values by implementing the ParameterGenerator interface.

**To set dynamic parameter values to a report:**

1. Create a class MyParameterGeneratorImpl to implement the ParameterGenerator interface. See the API demo DemoParameterGenerator.java in  `<install_root>\help\samples\APIParameter` for an example of implementing the ParameterGenerator interface.
2. Add the class path into the class path of your implementation of running or scheduling the report such as DemoParameterRunReport.
3. In DemoParameterRunReport, replace the way of setting static parameter values and instead set dynamic values of the required parameters in the report. Take the parameter PToday for example:

   First disable or delete the line:

   `props.put(APIConst.TAG_PARAM_PREFIX + "PToday", "2007-5-21");`

   and then add a line as follows:

   `props.put(APIConst.TAG_PARAM_PREFIX + "PToday", APIConst.TAG_PARAM_GEN_PREFIX + "MyParameterGeneratorImpl";`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686282-Applying-a-User-Defined-CSS-to-an-HTML-Result-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712221-Specifying-Report-Running-Properties-in-the-Session)
