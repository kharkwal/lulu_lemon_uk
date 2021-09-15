import re
def hrefExtractor(raw_html):
    try:

        links = re.findall(r'(?i)href=[\"\']([^<>]*?)[\"\']', raw_html, re.MULTILINE | re.DOTALL)

        return links
    except Exception as e:
        print("Error at hrefExtractor = ", e)


def url_keyword_filtering(input_url, url_keyword_str):
    try:
        '''return  true if url matched else false'''
        url_keyword_lst = url_keyword_str.split('|')
        if 'http' in input_url:
            if re.search(url_keyword_lst[0], input_url, re.IGNORECASE) and re.search(url_keyword_lst[1], input_url,
                                                                                     re.IGNORECASE):
                if re.search(url_keyword_lst[2], input_url, re.IGNORECASE) and re.search(url_keyword_lst[3], input_url,
                                                                                         re.IGNORECASE):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        print("Error at :", e)