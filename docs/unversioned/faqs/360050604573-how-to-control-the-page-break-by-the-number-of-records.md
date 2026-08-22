---
title: "How to control the page break by the number of records"
id: 360050604573
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050604573-How-to-control-the-page-break-by-the-number-of-records
updated_at: 2023-02-10T01:29:07Z
---

# How to control the page break by the number of records

### Overview

Page reports display the number of records on each page dynamically by default.  The number of records is determined by the page size and content.  To override this functionality, you can write a formula to control the number of records displayed on each page.

### Solution

Follow these steps to create a formula to control the number of records on each page of the report:

1. Define and initialize the global record number.  Use the following code and insert it into the report header section:  

   ```
      global integer num;  
      num=0;
   ```
2. Calculate the record number by incrementing the global record variable initialized in the previous step.  Use the following code and insert it into the detail section:  

   ```
   num=num+1;
   ```

   You can set the property "invisible" to **true** in the report template so the value is not displayed.
3. Determine how many records to show on each page by controlling the behavior when the global record variable reaches a specific count.  For example, use the following code to control the **On New Page** detail section property to show 10 records per page:  

   ```
   if (remainder(num,10)==0 && num!=0) return true  
   else return false
   ```
