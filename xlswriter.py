import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet("santosh")

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(12, 0, 123)
worksheet.write(3, 0, 123.456)


# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()
