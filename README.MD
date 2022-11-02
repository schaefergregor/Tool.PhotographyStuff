# MyPhotographTools

I'm using this tools for different stuff. Mostly I create different folders for different cameras/smartphones. When the work is finished, I use the scripts for deleting converted files, movies, etc.

## My Folder-Structure

<code>
    <pre>
|- Main_Travel_Folder
    |- Travel_Day_1
        |- camera
            |- DSC_0001.NEF
            |- DSC_0002.NEF
            |- DSC_0003.NEF
            |- convert
                |- DSC_0001.JPG
                |- DSC_0002.JPG
                |- DSC_0003.JPG
        |- mobile
    |- Travel_Day_2
        |- camera
            |- DSC_0004.NEF
            |- DSC_0005.NEF
            |- DSC_0006.NEF
            |- convert
                |- DSC_0004.JPG
                |- DSC_0005.JPG
                |- DSC_0006.JPG
        |-- mobile
    </pre>
</code>

### How to use
Copy the Python-Script into **Main_Travel_Folder**. The tools are just working with the specific folder structure.

<code>
python script_name.py
</code>

## Future Plans
* Python NEF-Converter for automated convertion.
* Delete Raw-Files older than X-days (cleanup)
