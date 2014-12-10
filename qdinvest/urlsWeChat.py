from django.conf.urls import patterns, url
import viewWechat

urlpatterns = patterns('',
	url(r'^$', viewWechat.Index, name='Index'),
	url(r'^reg/$', viewWechat.Register, name='Register'),
	url(r'^forget/$', viewWechat.Forget, name='Forget'),
	url(r'^index/$', viewWechat.Index, name='Index'),
	url(r'^prolist/(\d+)$', viewWechat.GetProList, name='GetProList'),
	url(r'^prodetail/t(\w)d(\d+)$', viewWechat.ProDetail, name='ProDetail'),
	url(r'^nodetail/t(\w+)d(\d+)$', viewWechat.NoticeDetail, name='NoticeDetail'),
	url(r'^like/$', viewWechat.ProLike, name='ProLike'),
	url(r'^promanage/t(\w+)d(\d+)$', viewWechat.ProManage, name='ProManage'),
	url(r'^pd/t(\w+)d(\d+)$', viewWechat.ProjectDetail, name='ProjectDetail'),
	url(r'^login/$', viewWechat.Login, name='Login'),
	url(r'^logout/$', viewWechat.Logout, name='Logout'),
	url(r'^account/$', viewWechat.Personal, name='Personal'),
	url(r'^setting/$', viewWechat.Setting, name='Setting'),
	url(r'^mypro/$', viewWechat.GetMyProList, name='GetMyProList'),
	url(r'^mylike/$', viewWechat.GetMyLikeProList, name='GetMyLikeProList'),
	url(r'^myproinvest/t(\w+)d(\d+)$', viewWechat.GetMyProInvest, name='GetMyProInvest'), 
	url(r'^invest/$', viewWechat.Invest, name='Invest'), 
	url(r'^feedback/$', viewWechat.Feedback, name='Feedback'),
	url(r'^pop/$', viewWechat.Pop, name='Pop'),
	url(r'^nodetail/t(\w+)d(\d+)$', viewWechat.NoticeDetail, name='NoticeDetail'),
	url(r'^instructions/$', viewWechat.PRO_Instructions, name='PRO_Instructions'), 
	url(r'^investor/$', viewWechat.PRO_Investor, name='PRO_Investor'), 
	url(r'^profit_select/$', viewWechat.Profit_Select, name='Profit_Select'), 
	)