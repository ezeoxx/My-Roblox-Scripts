--Admin On Steroids V1 (Beta)
getgenv().autokill = false;

function KillAll()
    spawn(function()
        while getgenv().autokill == true do
            for i,v in pairs(game:GetService("Players"):GetDescendants()) do
                if v.Name ~= game.Players.LocalPlayer.Name and v.ClassName == "Player" then
                    local args = {[1] = ":explode "..v.Name.." "}
                    game:GetService("ReplicatedStorage").HDAdminClient.Signals.RequestCommand:InvokeServer(unpack(args))
                    local args = {[1] = "Just exploded "..v.Name.." :D",[2] = "All"}
                    game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(unpack(args))
                    wait(3.5)
                end
            end
        end
    end)
end

local library = loadstring(game:HttpGet("https://raw.githubusercontent.com/bloodball/-back-ups-for-libs/main/Splix"))()

local window = library:new({textsize = 13.5,font = Enum.Font.RobotoMono,name = "Admin On Steroids",color = Color3.fromRGB(225,58,81)})

local tab = window:page({name = "Menance"})

local section1 = tab:section({name = "Fun Stuff",side = "left",size = 250})


section1:toggle({name = "Kill All",def = false,callback = function(value)
  getgenv().autokill = value
  KillAll()
end})

section1:button({name = "UnControl",callback = function()
    local args = {[1] = ":uncontrol",[2] = "All"}
    game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(unpack(args))
end})

--section1:slider({name = "rate ui lib 1-100",def = 1, max = 100,min = 1,rounding = true,ticking = false,measuring = "",callback = function(value)
  -- print(value)
--end})

--section1:dropdown({name = "dropdown",def = "",max = 10,options = {"1","2","3","4","5","6","7","8","9","10"},callback = function(chosen)
 --  print(chosen)
--end})
-- for dropdowns put max to the number of items u have in the opions

--section1:buttonbox({name = "buttonbox",def = "",max = 4, options = {"yoyoyo","yo2","yo3","yo4"},callback = function(value)
  -- print(value)
--end})


--section1:multibox({name = "multibox",def = {}, max = 4,options = {"1","2","3","4"},callback = function(value)
   --print(value)
--end})

--section1:textbox({name = "textbox",def = "default text",placeholder = "Enter WalkSpeed",callback = function(value)
--   print(value)
--end})

section1:keybind({name = "Set UI Key",def = nil,callback = function(key)
   window.key = key
end})

--local picker = section1:colorpicker({name = "color",cpname = nil,def = Color3.fromRGB(255,255,255),callback = function(value)
   --color = value
--end})
