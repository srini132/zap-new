from utils import (
    check_url_response,
    check_http_headers,
    extract_forms,
    find_common_vuln_patterns,
    port_scan
)

if __name__ == "__main__":
    target = input("Enter URL (e.g. https://example.com): ")
    host = target.replace("http://", "").replace("https://", "").split("/")[0]

    response = check_url_response(target)

    if response:
        check_http_headers(response.headers)
        extract_forms(response.text)
        find_common_vuln_patterns(response.text)
        port_scan(host)
