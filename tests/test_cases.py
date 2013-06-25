import os

CASEDIR = os.path.join("support", "cases")
websites = os.listdir(CASEDIR)
for website in websites:
    website_dir = os.path.join(CASEDIR, website)
    for sub_website in os.listdir(website_dir):
        sub_website_dir = os.path.join(website_dir, sub_website)
        basenames = set([filename.split('.')[0] for filename in os.listdir(sub_website_dir)])
        for basename in basenames:
            print os.path.join(sub_website_dir, basename + '.js')

#   Dir[File.join(cases_dir, "*")].each do |page_dir|
#   describe page_dir.split("/")[-2..-1].join("/") do
#       Dir[File.join(page_dir, "*")].keep_if { |f| f =~ /([.]html$)/ }.each do |html_file|
#         it "#{html_file.split("/").last}" do
#           pending "These are dynamic tests that are not yet passing so commenting out for now"
#           # json_file = html_file.gsub(/([.]html$)/, ".js")
#           # html = open(html_file).read
#           # json = open(json_file).read

#           # JSON.parse(Microformats2.parse(html).to_json).should == JSON.parse(json)
#         end
#       end
#     end
#   end

