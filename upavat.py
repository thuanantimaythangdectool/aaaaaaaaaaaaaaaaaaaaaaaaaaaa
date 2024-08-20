import requests,json
session = requests.Session()
def GetUIDAnh(Cookie,ANH):
    headers = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi','cookie': Cookie,'sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','viewport-width': '1366',}
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    uid=Cookie.split("c_user=")[1].split(';')[0]
    params = {
        'profile_id': uid,
        'photo_source': '57',
        'av': uid,
        '__user': uid,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        '__a': '1',
        '__req': '1d',
        '__hs': '19568.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1007929669',
        '__s': '9upeo9:ym47fb:rildfi',
        '__hsi': '7261687967184274031',
        '__dyn': '7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DU6u0luq7oc81xoswIK1Rwwwg8a8465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G4UfovwRwlE-U2exi4UaEW2au1jxS6FobrwKxm5oe8cEW4-5pUfEdfws9ovUy2a0SEuBwJCwLyESE7i3C223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo2aw',
        '__csr': 'hA5can6Nnkl5lAdskBGBaNAn59RbRHlIWmCxymg8ERpkTHKGHJHt4QClp2v-iiyaFqCmDQRWBGbLhqbiYCbStADEwJoSUDy8yQV9d7WBqyaCh9-UDCyWQ8Kbypq-p6GqUyFRGdjBhei8xvAzKvx28K5vhEK8zUNebxecADzUgUigLBF1e8QmbyUoGqhanCyUx28K2C6ElwPG22bKcg8o462y5oboepUCmu8K8AwBKiayo89E4q2O2O3i2e4otyFU-8wiK2ObwMzUW2CazQ6VU2Cx2686rG5E4S9w3goO03tt01Mm025W01_Pw0VHw0zLyo8Vk0FE3TwbS0deg0lxc07RU1CFJ017ow6C0jt056CjGdw2Eeh1a9mkk0cxw1EC0dQ82q0jq0dxwaK0FU2uyo1ao2My826wt80w-0ga0wEy2-0A80EZ0',
        '__comet_req': '15',
        '__spin_r': '1007929669',
        '__spin_b': 'trunk',
    }
    response = session.post(
        'https://www.facebook.com/profile/picture/upload/',
        params=params,
        headers=headers,
        files={"file": (f"{ANH}",open(f"{ANH}","rb"))},
    ).text.split("(;;);")[1]
    json_response = json.loads(response)
    payload = json_response["payload"]
    fbid = payload["fbid"]
    return fbid
cookie='sb=ReS5ZguiXTHo8o9288VDis6R; datr=ReS5ZuShkyIs-iLd1vioGMq6; ps_l=1; ps_n=1; locale=vi_VN; c_user=61563479217760; fr=1OusDBIdxjkfDKL70.AWV8q8F4a93AHT42SdQRErfMXR0.BmxFR3..AAA.0.0.BmxFUK.AWUpd7c88lM; xs=12%3A7LNOXVO2ofa0_Q%3A2%3A1724142861%3A-1%3A-1; wd=1437x953; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1724143294843%2C%22v%22%3A1%7D'
a=GetUIDAnh(cookie,'D:\\302697037_583865803489429_5100099679707137555_n.jpg')
print(a)
