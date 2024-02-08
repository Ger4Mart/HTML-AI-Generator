def save_html_file(html_content, file_name="template.html"):
    with open(file_name, "w") as file:
        file.write(html_content)
    print(f"HTML file '{file_name}' has been created successfully.")

def generate_html_template(title, elements, classes, include_section, include_table):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
"""

    if include_section:
        html_content += """<section class="content">\n"""

    for element, class_name in classes.items():
        if element == 'heading':
            html_content += f"""    <h1{' class="' + class_name + '"' if class_name else ''}>This is a heading</h1>\n"""
        elif element == 'paragraph':
            html_content += f"""    <p{' class="' + class_name + '"' if class_name else ''}>This is a paragraph.</p>\n"""
        elif element == 'image':
            html_content += f"""    <img src="image.jpg" alt="Image"{' class="' + class_name + '"' if class_name else ''}>\n"""
        elif element == 'link':
            html_content += f"""    <a href="https://example.com"{' class="' + class_name + '"' if class_name else ''}>Link to example.com</a>\n"""
        elif element == 'table':
            html_content += """    <table>\n"""
            html_content += """        <tr>\n"""
            html_content += """            <th>Header 1</th>\n"""
            html_content += """            <th>Header 2</th>\n"""
            html_content += """        </tr>\n"""
            html_content += """        <tr>\n"""
            html_content += """            <td>Data 1</td>\n"""
            html_content += """            <td>Data 2</td>\n"""
            html_content += """        </tr>\n"""
            html_content += """    </table>\n"""

    if include_section:
        html_content += """</section>\n"""

    html_content += """</body>
</html>"""

    return html_content

if __name__ == "__main__":
    title = input("Enter the title of your HTML page: ")
    print("Choose elements to include in your HTML file:")
    print("1. Heading")
    print("2. Paragraph")
    print("3. Image")
    print("4. Link")
    print("5. Section")
    print("6. Table")
    print("0. Quit")

    choices = []
    while True:
        choice = input("Enter your choice (0/1/2/3/4/5/6): ")
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4', '5', '6','0']:
            choices.append(choice)
        else:
            print("Invalid choice.")

    if not choices:
        print("No elements selected. Exiting program.")
    else:
        elements_to_include = []
        include_section = False
        include_table = False
        for choice in choices:
            if choice == '1':
                elements_to_include.append('heading')
            elif choice == '2':
                elements_to_include.append('paragraph')
            elif choice == '3':
                elements_to_include.append('image')
            elif choice == '4':
                elements_to_include.append('link')
            elif choice == '5':
                include_section = True
            elif choice == '6':
                include_table = True

        classes = {}
        for element in elements_to_include:
            class_name = input(f"Enter the Title {element} (leave blank for no title): ")
            classes[element] = class_name.strip()

        html_content = generate_html_template(title, elements_to_include, classes, include_section, include_table)
        save_html_file(html_content,f"{title}.html")
