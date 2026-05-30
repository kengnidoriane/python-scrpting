C:/my-directory/my-file.txt
C:\\my-directory\\my-file.txt
C:/my-directory/my-file.txt 
# in Python, we can use either forward slashes (/) or double backslashes (\\) to specify file paths. Both of these are valid and will work on all operating systems. However, using forward slashes is generally recommended as it is more consistent and easier to read. Additionally, using forward slashes can help avoid issues with escape characters that can arise when using backslashes.
outputs['path_value']= os.environ.get("PATH")