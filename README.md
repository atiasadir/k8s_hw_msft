# K8S - HW<br>

# Cluster details:<br>
<b>a</b>. Use Azure and AKS-Engine (not pre-defined AKS solutions)<br>
<b>b</b>. Set up K8S latest cluster, with RBAC enabled.<br>
<b>c</b>. Cluster should have 2 services – A and B.<br>
<b>d</b>. Cluster should have Ingress controller, redirecting traffic by URL: xxx/serviceA or xxx/serviceB<br>
<b>e</b>. ServiceA should not be able to talk with ServiceB (policy disabled)<br>
<b>f</b>. For Service A:write a script\application which retrieves the bitcoin value in dollar<br>
   From an API on the web (you should find one), every minute and prints it,<br>
   Also every 10 minutes it should print the average value of the last 10 minutes<br>

# General Guideline:<br>
<b>a</b>. Consider this as process for setting up “production-ready” cluster by all meaning<br>
<b>b</b>. The following cluster buildout should be automated and fully repeatable<br>
<b>c</b>. Share cluster templates and yaml files as GitHub repo / zip file<br>
