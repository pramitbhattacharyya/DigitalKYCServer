package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Process p;
        try {
            String filename="/home/pramit/Desktop/Developers/Try/Test/orig_IMG_2.jpg",isdl="1";
            String[] cmd = { "/bin/sh","-c","/home/pramit/IdeaProjects/DigitalKYCServer/src/com/company/crop_n_rotate.py "
                    +filename+" "+isdl};

            p = Runtime.getRuntime().exec(cmd);
            BufferedReader reader=new BufferedReader(new InputStreamReader(
                    p.getInputStream()));
            p.waitFor();
            String z=String.valueOf(p.exitValue());
            System.out.println("z= "+z);
            String line;
            while((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

}