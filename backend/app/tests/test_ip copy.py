import requests

def get_ip_via_http():
    """
    通过 HTTP API 获取本机公网出口 IP。
    依赖: pip install requests
    """
    # 备用 API 列表，防止单一节点失效
    api_list = [
        'https://4.ipw.cn',             # 国内高可用 API (IPv4)
        'https://api.ipify.org',        # 国际通用 API
        'https://ifconfig.me/ip'        # 国际通用 API
    ]
    
    for api_url in api_list:
        try:
            # 设置 3 秒超时，避免阻塞
            response = requests.get(api_url, timeout=3)
            response.raise_for_status()
            ip_address = response.text.strip()
            
            # 简单验证返回的是否非空
            if ip_address:
                return ip_address
        except requests.exceptions.RequestException:
            # 当前 API 失败，静默尝试下一个
            continue
            
    print("所有 HTTP IP 获取接口均请求失败。")
    return None

if __name__ == '__main__':
    print(get_ip_via_http())