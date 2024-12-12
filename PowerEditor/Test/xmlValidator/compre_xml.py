#!/usr/local/bin/python3

import os
import io
import sys

import requests
from hashlib import sha256
from lxml import etree


def parse_xml_file(filename_xml):

    # open and read schema file
    #with open(filename_xsd, 'r') as schema_file:
        #schema_to_check = schema_file.read()

    # open and read xml file
    #with open(filename_xml, 'r') as xml_file:
    #    xml_to_check = xml_file.read()

    # parse xml
    try:
        doc = etree.parse(filename_xml)
        #print(f'{filename_xml} XML well formed, syntax ok.')
        return doc
    # check for file IO error
    except IOError:
        #print('Invalid File')
        post_error(f'{filename_xml}: IOError Invalid File')


    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
        #print('XML Syntax Error, see error_syntax.log')
        post_error(f'{filename_xml}: {str(err.error_log)}: XMLSyntaxError Invalid File')

    # check for general XML errors
    except etree.LxmlError as err:
        #print('XML Error, see error_syntax.log')
        post_error(f'{filename_xml}: {str(err.error_log)}: LxmlError Invalid File')

    except:
        #print('Unknown error.')
        post_error(f'{filename_xml}: Unknown error. Maybe check that no xml version is in the first line.')
    return None


# 获取所有具有 id 属性的叶子节点的 id 值
def get_leaf_node_ids(root):
    id_name_map = {}
    def traverse(node):
        if len(node) == 0 and 'id' in node.attrib:
            id_name_map[node.attrib['id']] = node.attrib.get('name', 'N/A')
        for child in node:
            traverse(child)
    traverse(root)
    return id_name_map
    
# 比较两个 XML 文件的叶子节点 id
def compare_xml_files(file1, file2):
    file1 = os.path.join("../../installer/nativeLang", file1)
    file2 = os.path.join("../../installer/nativeLang", file2)
    root1 = parse_xml_file(file1).getroot()
    root2 = parse_xml_file(file2).getroot()

    id_name_map1 = get_leaf_node_ids(root1)
    id_name_map2 = get_leaf_node_ids(root2)
    
    ids1 = set(id_name_map1.keys())
    ids2 = set(id_name_map2.keys())
    
    compare_logs = (f"{file1} 节点数量    {len(ids1)}\n")
    compare_logs = compare_logs + (f"{file2} 节点数量    {len(ids2)}")

    # 查找在第一个文件中存在但在第二个文件中不存在的 id
    missing_ids = ids1 - ids2

    return missing_ids, id_name_map1, compare_logs
if __name__ == "__main__":
    import sys
    # E:\npp\PowerEditor\installer\nativeLang\english.xml
    print( len(sys.argv) )
    if len(sys.argv) > 2:
        file1 = sys.argv[1] + ".xml"
        file2 = sys.argv[2] + ".xml"
    elif len(sys.argv) > 1:
        file2 = sys.argv[1] + ".xml"
    else:
        # python compre_xml.py japanese
        print("Usage: python compre_xml.py chineseSimplified")
        # parse_xml_files_from_nativeLang_dir()
        # 示例 XML 文件路径
        file2 = 'chineseSimplified.xml'
    cnt = 0
    if len(sys.argv) > 2:
        # 比较并输出结果
        missing_ids, id_name_map1, compare_logs= compare_xml_files(file1, file2)
        if len(missing_ids) > 0:
            print(compare_logs)
            print(f"Messing ids count: {len(missing_ids)}")
            for id in missing_ids:
                print(f"id: {id}        name: {id_name_map1[id]}")
            cnt += 1    
            print(f'------------------------------------------------Done    {cnt}.')
    else:
        for file in os.listdir("../../installer/nativeLang"):
            if file.endswith(".xml"):
                # print(os.path.join("../../PowerEditor/installer/nativeLang", file))
                file1 = file
                if file1 != file2:
                    # 比较并输出结果
                    missing_ids, id_name_map1, compare_logs= compare_xml_files(file1, file2)
                    if len(missing_ids) > 0:
                        print(compare_logs)
                        print(f"Messing ids count: {len(missing_ids)}")
                        for id in missing_ids:
                            print(f"id: {id}        name: {id_name_map1[id]}")
                        cnt += 1    
                        print(f'------------------------------------------------Done    {cnt}.')

    
    
    
