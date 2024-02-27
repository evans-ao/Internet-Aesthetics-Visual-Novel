#This is just to see if I have a way to get the forums in files for automatic generation...or at least to start working on that

init python:
    
    def get_thread_stuff(filename):
        #the goal here is to have a tab delimited .txt file that contains each thread
        #that way we don't have to add every single thread manually
        #f=renpy.open_file(filename)
        #for l in f:
        #    l = l:[-1]
        #    threadstuff=l.split('\t')
        #f.close()
        #return threadstuff
        pass

    def make_the_thread(threadstuff):
        pass
        #threadstuff should follow the format of: username  post    n   thread title
        #[username here]   [post here]    [n here]  [thread title here]
        #[username here]   [post here]    [n here]
        #(n is a number indicating reply layer--0 for OG post, 1 for reply to that, 2 for reply to reply)
        #I assume that having a number to indicate a reply layer will be helpful; otherwise the posts are just in thread order




#Renpy Tom actually provided the below code in a forum post here: https://lemmasoft.renai.us/forums/viewtopic.php?t=5038
# python hide:
#     f = renpy.file("foo.txt", "tU")
#     for l in f:
#         l = l:[-1] # Strip off newline.
#         a = l.split('\t')
#         # The entries are now in a, with a[0] the first entry, a[1] the second entry, and so on.
#     f.close()