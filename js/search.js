// 实现前端搜索
$(document).ready(function() {
	$('button').click(function () {
		words = $('input').val(); //获取输入的词条,并分词
		word_array = words.split(' ');
		let res_html = {}; // 保存搜索结果
		res_html['has_word'] = []; //保存查询的词
		$.getJSON('js/article_index.json', function (result) { // 获得分词索引文件
			file_index = result['file_index']
			word_index = result['word_index']
			file_array = result['file_array']
			for (word_int in word_array) {	//在索引文件中查询到目标词,并构造数据保存格式
				word = word_array[word_int];
				if (word_index[word] == null) {
					continue
				} else {
					html_int_array = word_index[word]
				}
				let html_array = []
				for (i in html_int_array) {
					html_array[i] = file_array[html_int_array[i]]
				}
				res_html[word] = html_array
				res_html['has_word'].push(word) // console.log(word, html_array)
			}
			let html_str = '<div class="col"><ul>' //构造查询结果页面
			for (let word_int = 0; word_int < res_html['has_word'].length; word_int++) {
				words = res_html['has_word']
				word = words[word_int]
				console.log(word)
				html_str = html_str + '<li>' + word + '</li><ul>'
				for (a_int in res_html[word]) {
					a_href = res_html[word][a_int];
					a_str = '<a href="' + a_href + '">' + a_href + '</a>'
					html_str = html_str + '<li>' + a_str + '</li>'
				}
				html_str = html_str + '</ul>'
			}
			html_str = html_str + '</ul></div>'
			$('div.row.align-items-center ').html(html_str)

		});
	});
});
