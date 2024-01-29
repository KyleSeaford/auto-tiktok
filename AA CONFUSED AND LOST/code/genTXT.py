def gen():
    stories = int(input("How many stories do you want to generate? "))

    for i in range(stories):
        title = str(input("Enter the title: "))
        story = str(input("Enter the story: "))

        story = title + "\n\n" + story
        storyTXT = open("stories/story" + str(i + 1) + ".txt", "w")
        storyTXT.write(story)
        storyTXT.close()
        print("Story " + str(i + 1) + " generated.")
    
    print("All stories generated.")
    
gen()