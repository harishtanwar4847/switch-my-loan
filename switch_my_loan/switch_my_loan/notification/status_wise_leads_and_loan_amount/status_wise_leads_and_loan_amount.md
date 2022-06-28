Hello,
Please find the dashboard for Status-wise Leads and Loan Amount:
<table border="1" cellspacing="0" cellpadding="5" align="">
<th>Sr.No.</th>
<th>Lead Status</th>
<th>Amount</th>
<th>No. of Cases</th>
{% for j in doc.leads %}
<tr>
<td>{{loop.index}}</td>
<td>{{j[0]}}</td>
<td>{{j[1]}}</td>
<td>{{j[2]}}</td>
</tr>
{% endfor %}
</table>
