// Textarea row for blog creation
var textArea = document.getElementById('id_body_text');
textArea.cols = "100";

var textArea = document.getElementById('id_description');
textArea.cols = "100";

var inputTags = document.getElementsByTagName('input');

for (var index = 0; index < inputTags.length; index++){
		var elem = inputTags[index];
		elem.className = 'form-control';
	}
var select = document.getElementById('id_occupation');
select.className = 'form-control';



