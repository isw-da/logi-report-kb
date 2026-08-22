---
title: "Unexpected Report Session Expiration"
id: 360045464914
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360045464914-Unexpected-Report-Session-Expiration
updated_at: 2020-07-27T22:36:47Z
---

# Unexpected Report Session Expiration

### 

### What is the "Unexpected Report Session Expiration" problem?

If you are using a Logi Report Server version earlier than 15.6 Update 1 on Google Chrome version 71.x or above, then you may encounter this problem.  The error indicates that the report timed out earlier than expected.

### What is the cause of this issue?

Google Chrome versions later than 71.x require 'strict MIME type' by default, and some Logi Report build-in JavaScript files use .jz as the file extension, but .jz is not configured in the MIME.

### How to solve the problem?

* **For a standalone Logi Report server**: Modify the file content-type.properties located under %installroot\_LogiReportServer%\bin folder to include .jz as one of the file extensions:  
    
  application/x-javascript:\  
  file\_extensions=.js,.jz;
* **For an embedded environment**: Modify the file web.xml to include .jz in the **excludedFiles** parameter value:  

  ```
  <filter>  
     <filter-name>CharacterEncoding</filter-name>  
     <filter-class>jet.server.servlets.CharacterEncodingFilter</filter-class>  
     <init-param>  
        <param-name>encoding</param-name>  
        <param-value>UTF-8</param-value>  
     </init-param>  
     <init-param>  
        <param-name>excludedFiles</param-name>  
        <param-value>.css,.js,.jz</param-value>  
     </init-param>  
  </filter>
  ```
