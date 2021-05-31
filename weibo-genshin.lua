local log = require("log")
local Api = require("coreApi")
local json = require("json")
local http = require("http")

function ReceiveFriendMsg(CurrentQQ, data)
    return 1
end
function picurl()
pic = "http://网址/weibo.png"  
--这里填写你在getfull.py中修改的网站路径的网站访问链接（访问到图片，比如网站链接是www.baidu.com，
--getfull.py中的网站路径是"网站根目录/img/weibo.png"那么这里就填写“http://www.baidu.com/img/weibo.png”
     return pic
    end
function ReceiveGroupMsg(CurrentQQ, data)
    picurl()
    if (string.find(data.Content, "原神微博") == 1) then
        luaRes =
            Api.Api_SendMsg(
            CurrentQQ,
            {
                toUser = data.FromGroupId,
                sendToType = 2,
                sendMsgType = "PicMsg",
                groupid = 0,
                content = "\n原神的最新微博qwq",
                atUser = 0,
                picUrl = pic   
            }
        )
    end
    return 1
end
function ReceiveEvents(CurrentQQ, data, extData)
    return 1
end