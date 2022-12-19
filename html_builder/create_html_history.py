"""
Builds an html template and interpolates the data
returned by the queries
    TODO: enum tag builder
"""
from history_queries import query_history


def build_html_file():
    rows = query_history.select_all_records()
    html_result = f'<!doctype html>\n<html>\n\t<head>\n\t\t<title>History Stats</title>\n\t</title>'
    f'\n\t<link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.21.2/dist/bootstrap-table.min.css">' \
        f'\n</head>\n<body>\n'

    for row in rows:
        html_result += f'<table class = "table">\n\t<tr>\n\t<td>{row[0].encode("utf-8")}</td><td>{row[1]}</td>\n\t' \
                       f'</tr>\n\t'

        """
        Prints the content of the file for debug purposes
        
        file = codecs.open("history_stats.html", 'r', "utf-8")
        print(file.read())
        """

    html_result += '</table>\n\t</body>\n</html>'
    html_file = open('history_stats.html', 'w')
    html_file.write(html_result)
    html_file.close()

