from xml.etree import ElementTree as ET

root = ET.Element('task')
day = ET.SubElement(root, 'day')
day.set('date', '01.01.2024')
task1 = ET.SubElement(day, "task")
task1.text = "Wake UPPP"
task2 = ET.SubElement(day, "task")
task2.text = "Make coffe"
tree = ET.ElementTree(root)
tree.write("task.xml")
