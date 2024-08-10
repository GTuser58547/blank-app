import streamlit as st

# 设置页面配置
st.set_page_config(layout="wide")

# 使用 CSS 设置全局样式
st.markdown("""
    <style>
    .main {
        padding-top: 50px;   /* 设置上边距 */
        padding-bottom: 50px;  /* 设置下边距 */
        max-width: 1000px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).（左边这儿是开发者看的。）"
)
st.write("下面这些怎么样？")
st.markdown("一个可能用得上的工具网站[你可以点一下](https://www.jyshare.com)")
st.markdown("不知道你想不想玩玩小游戏[点这里](https://www.yikm.net)")
st.markdown("或者自己做个小游戏也行[确实](https://www.construct.net/en)")
