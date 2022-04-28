Hello,<br>
These Leads Remains Unattended yesterday:<br><br>
<table border="1" cellspacing="0" cellpadding="5" align="">
<th>Lead ID</th>
<th>Name</th>
<th>Mobile Number</th>
{% for j in doc.leads %}
<tr>
<td>{{j[0]}}</td>
<td>{{j[1]}}</td>
<td>{{j[2]}}</td>
</tr>
{% endfor %}
</table>
