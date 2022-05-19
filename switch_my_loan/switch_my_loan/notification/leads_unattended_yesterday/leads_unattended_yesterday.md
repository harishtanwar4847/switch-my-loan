Hello,<br>
These Leads Remains Unattended yesterday:<br><br>
<table border="1" cellspacing="0" cellpadding="5" align="">
<th>S. No.</th>
<th>Lead ID</th>
<th>Lead Name</th>
<th>Loan Amount</th>
<th>Product</th>
<th>Lead Creation Time & Date</th>
<th>Sales Manager Allocated Source</th>
{% for j in doc.leads %}
<tr>
<td>{{loop.index}}</td>
<td>{{j[0]}}</td>
<td>{{j[1]}}</td>
<td>{{j[2]}}</td>
<td>{{j[3]}}</td>
<td>{{j[4]}}</td>
<td>{{j[5]}}</td>
</tr>
{% endfor %}
</table>