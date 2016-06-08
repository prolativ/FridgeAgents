var VerticalHeaderTableModule = function() {
	var table = $("<table>");
	var tbody = $("<tbody>");
	table.append(tbody);
	$("body").append(table);

	this.render = function(data) {
		this.reset();

		var header = data.header;
		var values = data.values;
		var formattings = data.formattings

		for(var i = 0; i < header.length; ++i) {
    	var row = $("<tr>");
			var rowHeader = $("<th>");
     	var headerTitle = header[i];
     	rowHeader.append(headerTitle);
			row.append(rowHeader);
			for(var j = 0; j < values.length; ++j) {
				var dataCell = $("<td>");
				dataCell.append(values[j][headerTitle]);
				var color = formattings[j].color;
				if(color) {
					dataCell.css("color", color);
				}
				var bold = formattings[j].bold;
				if(bold) {
					dataCell.css('font-weight', 'bold')
				}
				dataCell.css("width", "30px")
				row.append(dataCell);
			};
			tbody.append(row);
		}
	};

	this.reset = function() {
		tbody.html("");
	};
};