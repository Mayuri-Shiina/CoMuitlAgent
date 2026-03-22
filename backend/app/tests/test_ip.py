import stun

def get_ip_via_stun():
    try:
        # 显式指定 STUN 服务器，例如腾讯或小米的公共服务器
        # 备选服务器：stun.qq.com, stun.miwifi.com, stun.stunprotocol.org
        nat_type, external_ip, external_port = stun.get_ip_info(
            stun_host='stun.qq.com', 
            stun_port=3478
        )
        return external_ip
    except Exception as e:
        print(f"STUN 获取失败: {e}")
        return None

if __name__ == '__main__':
    print(get_ip_via_stun())