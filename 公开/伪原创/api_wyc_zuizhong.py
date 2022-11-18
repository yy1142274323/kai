
###############################################################################
#
# Spin Rewriter API for Python >= 3 (PyPi) example of how to
# generate unique variation.
#
# Note: Spin Rewriter API server is using a 120-second timeout.
# Client scripts should use a 150-second timeout to allow for HTTP connection
# overhead.
#
# SDK Version    : v1.0
# Language       : Python 3
# Dependencies   : spin-rewriter-api
# Website        : https://www.spinrewriter.com/
# Contact email  : info@spinrewriter.com
#
# SDK Author     : Bartosz Wójcik (https://www.pelock.com)
#
###############################################################################

#
# include Spin Rewriter API module
#
from spinrewriterapi import SpinRewriterAPI
import pymysql

def ci(x):
    # your Spin Rewriter email address goes here
    email_address = "Ivellioshp01@yahoo.com"

    # your unique Spin Rewriter API key goes here
    api_key = "aa4ec0b#fbcdd49_90451f6?3d49640"

    # Spin Rewriter API settings - authentication:
    spinrewriter_api = SpinRewriterAPI(email_address, api_key)

    #
    # (optional) Set a list of protected terms.
    # You can use one of the following formats:
    # - protected terms are separated by the '\n' (newline) character
    # - protected terms are separated by commas (comma-separated list)
    # - protected terms are stored in a Python [] array
    #
    protected_terms = "John, Douglas Adams, then"
    # protected_terms = "John\nDouglas\nAdams\nthen"
    #protected_terms = ["John", "Douglas", "Adams", "then"]

    spinrewriter_api.set_protected_terms(protected_terms)

    # (optional) Set whether the One-Click Rewrite process automatically protects
    # Capitalized Words outside the article's title.
    # ＃（可选）设置一键重写过程是否自动保护
    # 文章标题之外的＃个大写单词。
    spinrewriter_api.set_auto_protected_terms(False)

    # (optional) Set the confidence level of the One-Click Rewrite process.
    # （可选）设置一键重写过程的置信度。
    spinrewriter_api.set_confidence_level("medium")

    # (optional) Set whether the One-Click Rewrite process uses nested spinning syntax (multi-level spinning) or not.
    #（可选）设置一键重写过程是否使用嵌套旋转语法（多级旋转）。
    spinrewriter_api.set_nested_spintax(True)

    # (optional) Set whether Spin Rewriter rewrites complete sentences on its own.
    # （可选）设置Spin Rewriter是否自行重写完整的句子。
    spinrewriter_api.set_auto_sentences(True)

    # (optional) Set whether Spin Rewriter rewrites entire paragraphs on its own.----------------------------------6666
    # （可选）设置Spin Rewriter是否自行重写整个段落。
    spinrewriter_api.set_auto_paragraphs(False)

    # (optional) Set whether Spin Rewriter writes additional paragraphs on its own.--------------------------------------11111NNNNNNNNNNNNNNNNNN
    # （可选）设置Spin Rewriter是否自行编写其他段落。
    spinrewriter_api.set_auto_new_paragraphs(True)

    # (optional) Set whether Spin Rewriter changes the entire structure of phrases and sentences.
    # （可选）设置Spin Rewriter是否更改短语和句子的整个结构。
    spinrewriter_api.set_auto_sentence_trees(True)

    # (optional) Sets whether Spin Rewriter should only use synonyms (where available) when generating spun text.---------------------------------------------------11111
    # （可选）设置在生成旋转文本时，Spin Rewriter是否仅应使用同义词（如果可用）。
    spinrewriter_api.set_use_only_synonyms(False)

    # (optional) Sets whether Spin Rewriter should intelligently randomize the order of paragraphs and lists when
    # generating spun text.
    # ＃（可选）设置
    # ＃生成旋转文本
    # 时，Spin Rewriter是否应智能地随机化段落和列表的顺序。spinrewriter_api 。set_reorder_paragraphs （False ）
    # ＃（可选）设置Spin Rewriter是否应该自动丰富带有标题，布尔点等的生成文章
    spinrewriter_api.set_reorder_paragraphs(False)

    # (optional) Sets whether Spin Rewriter should automatically enrich generated articles with headings, bulpoints, etc.
    # （可选）设置Spin Rewriter是否应该自动丰富带有标题，布尔点等的生成文章
    spinrewriter_api.set_add_html_markup(False)

    # (optional) Sets whether Spin Rewriter should automatically convert line-breaks to HTML tags.
    # （可选）设置Spin Rewriter是否应将换行符自动转换为HTML标签。
    spinrewriter_api.set_use_html_linebreaks(False)

    # Make the actual API request and save the response as a native JSON object.
    text = x


    # Make the actual API request and save the response as a native JSON dictionary or False on error
    result = spinrewriter_api.get_unique_variation(text)

    if result:
        # print("Spin Rewriter API response")
        # print(result)
        r = result['response']
        print(r)
        sss2(r)
    else:
        print("Spin Rewriter API error")







#本地
def sss1():
    # 连接数据库
    connect = pymysql.Connect(
        host='115.159.212.84',
        user='yy677',
        passwd='677688',
        db='mytest'
    )

    # 获取游标
    cursor = connect.cursor()
    sql = "SELECT keyword FROM task_list where status=0 "

    cursor.execute(sql)
    a = cursor.fetchall()
    for i in a:
        x = i[0]
        print(x)
        ci(x)

    # 关闭连接
    connect.commit()



#网站
def sss2(r):

    # 连接数据库
    connect = pymysql.Connect(
        host='162.215.255.143',
        user='puguaskl_samoway',
        passwd='kangta327422dltb',
        db='puguaskl_samoway'
    )

    # 获取游标
    cursor = connect.cursor()

    # 写入数据库********************************************把中间代码注释去掉配置下


    # sql = "INSERT IGNORE INTO 表名称 (表头1, 表头2) VALUES ('%s', '%s')"*********这条是注释
    sql = "INSERT IGNORE INTO wp_posts (post_content) VALUES ('%s')"
    # data = (数据1,数据2)*********这条是注释
    data = (r)#r是数据要存的 转换之后的
    cursor.execute(sql % data)

    # 写入数据库********************************************把中间代码注释去掉配置下
    # 关闭连接
    connect.commit()
s


# 'When individuals are busy with work or holiday buying, don't fail to remember to award yourself with actual specials at the correct time. From the very first shop to the here and now day with hundreds of branches in 19 states, Jet's is popular for its square deep-dish Detroit-style pizza. Naturally, apart from that, there are hand-thrown thin-crust pizzas and also New york city style pizzas, fresh salads, breads and treats. When getting right here is their dedication to quality components, one thing that will certainly never ever transform.'
# 'When people are busy with work or holiday shopping, don't forget to reward yourself with real delicacies at the right time. From the first store to the present day with hundreds of branches in 19 states, Jet's is famous for its square deep-dish Detroit-style pizza. Of course, other than that, there are hand-thrown thin-crust pizzas and New York style pizzas, fresh salads, breads and desserts. One thing that will never change when ordering here is their commitment to quality ingredients.'


if __name__ == '__main__':
    sss1()




