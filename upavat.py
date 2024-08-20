def upload(uid,cookie,fb_dtsg,jazoest,ANH):
    params = {
        'profile_id': uid,
        'photo_source': '57',
        'av': uid,
        '__user': cookie.split("c_user=")[1].split(";")[0],
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': lsd,
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
        '__spin_t': str(int(datetime.now().timestamp())),
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