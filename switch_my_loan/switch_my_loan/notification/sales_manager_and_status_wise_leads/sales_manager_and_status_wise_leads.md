Hello,<br>
Pleas find the dashboard for Sales Manager and status wise Leads:<br><br>
<table border="1" cellspacing="0" cellpadding="5" align="">
<th>Sr.No.</th>
<th>Lead Owner Name</th>
<th>Open (Amount in Crs.)</th>
<th>Call Done (Amount in Crs.)</th>
<th>Meeting Scheduled (Amount in Crs.)</th>
<th>Meeting Conducted (Amount in Crs.)</th>
<th>Partly Documents Collected (Amount in Crs.)</th>
<th>Documents Received (Amount in Crs.)</th>
<th>Lender Selection (Amount in Crs.)</th>
<th>Pending For Reporting Manager Approval (Amount in Crs.)</th>
<th>Login Done (Amount in Crs.)</th>
<th>Additional Doc Required (Amount in Crs.)</th>
<th>Sanctioned (Amount in Crs.)</th>
<th>Disbursement Doc List (Amount in Crs.)</th>
<th>Disbursement Doc Submitted (Amount in Crs.)</th>
<th>Disbursed (Amount in Crs.)</th>
<th>Amount Credited (Amount in Crs.)</th>
<th>Lead (Amount in Crs.)</th>
<th>Replied (Amount in Crs.)</th>
<th>Opportunity (Amount in Crs.)</th>
<th>Quotation (Amount in Crs.)</th>
<th>Lost Quotation (Amount in Crs.)</th>

{% for j in doc.leads %}
<tr>
<td>{{loop.index}}</td>
<td>{{j[0]}}</td>
<td>{{j[1]}}</td>
<td>{{j[2]}}</td>
<td>{{j[3]}}</td>
<td>{{j[4]}}</td>
<td>{{j[5]}}</td>
<td>{{j[6]}}</td>
<td>{{j[7]}}</td>
<td>{{j[8]}}</td>
<td>{{j[9]}}</td>
<td>{{j[10]}}</td>
<td>{{j[11]}}</td>
<td>{{j[12]}}</td>
<td>{{j[13]}}</td>
<td>{{j[14]}}</td>
<td>{{j[15]}}</td>
<td>{{j[16]}}</td>
<td>{{j[17]}}</td>
<td>{{j[18]}}</td>
<td>{{j[19]}}</td>
<td>{{j[20]}}</td>

</tr>
{% endfor %}
</table>
