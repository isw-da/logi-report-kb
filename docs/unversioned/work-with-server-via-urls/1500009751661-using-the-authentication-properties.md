---
title: "Using the Authentication Properties "
id: 1500009751661
section: "Work With Server via URLs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751661-Using-the-Authentication-Properties
updated_at: 2021-07-25T07:18:32Z
---

# Using the Authentication Properties 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751681-Creating-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server)

# Using the Authentication Properties

Logi Report Server requires that the user be authenticated before he can access any web pages, so when using URL to work on Logi Report Server, if you have not previously been authenticated you can include the authentication properties to pass in login credentials in the URL. This is a proprietary login protocol developed to make it easy to identify a user by passing along the login request in the URL along with the operation request.

The following authentication properties are defined that can be used to pass in the login credentials.

* **jrs.authorization**  
   Tag of the HTTP query field jrs.authorization.  
   Description: Loads the requested page with the specified credential information. This method is not recommended for use outside of a firewall, although it looks like it is encrypted it is not secure.  
   Format of the value of the HTTP query field: Base64-encoded (userID:password). For details about Base64 encoding, refer to <http://en.wikipedia.org/wiki/Base64>.  
   In the following examples, the user ID and password are both set as admin, so the value of the HTTP query field is Base64-encoded("admin:admin")="YWRtaW46YWRtaW4=".
  + `http://localhost:8888/jrserver?jrs.cmd=jrs.get_subnodes&jrs.authorization=YWRtaW46YWRtaW4%3D.`
  + `http://localhost:8888/jreport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Dashboard - Coffee Sales.dsh","ver":-1}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

* **jrs.auth\_uid and jrs.auth\_pwd**  
   Tags of HTTP query field: jrs.auth\_uid and jrs.auth\_pwd.  
   Description: Loads the requested page with the specified credential information.  
   Format of the value of the HTTP query field: jrs.auth\_uid=USER\_ID, jrs.auth\_pwd=PASSWORD.  
   Examples:
  + This URL requests the JSP page viewVersion.jsp with credentials passed in to log in user "scott" with password "tiger":  
    `http://localhost:8888/jinfonet/viewVersion.jsp?jrs.cmd=jrs.view_ver_def&jrs.rst_version=1&jrs.ver_suff=.pdf&jrs.report=/Payroll Report.cls&jrs.auth_uid=scott&jrs.auth_pwd=tiger`
  + This URL runs the dashboard with credentials passed in to log in user "scott" with password "tiger":  
    `http://localhost:8888/jreport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Dashboard - Coffee Sales.dsh","ver":-1}]}&jrs.auth_uid=scott&jrs.auth_pwd=tiger`

**Note:** JRServlet does not perform authentication check when an HTTP request has no jrs.cmd in the HTTP query in the root path of JRServlet, and also does not accept the jrs.authorization and jrs.auth\_uid & jrs.auth\_pwd for the request.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751681-Creating-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server)
