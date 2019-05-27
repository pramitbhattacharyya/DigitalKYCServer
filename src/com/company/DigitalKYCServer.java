package com.company;
/**
 *
 * @author PRAMIT
 */
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DigitalKYCServer extends javax.swing.JFrame {//implements Runnable{
    public DigitalKYCServer() {
    }
    public static void main(String args[]) {
        new DigitalKYCServer().onCreate();
    }
    public  void onCreate()
    {
        Thread serverThread=new Thread(new ServerThread());
        serverThread.start();
    }
    public class ServerThread implements Runnable{
        Socket s;
        ServerSocket ss;
        InputStreamReader isr;
        DataInputStream dis;
        BufferedReader br;
        PrintWriter pw;
        String message;
        String values[];
        StringBuffer sbr;
        int len;
        byte []data;
        String path="/home/pramit/Desktop/DigitalKYCPic/DigitalKyc";
        String Imgpath="";
        @Override
        public void run() {
//            java.awt.EventQueue.invokeLater(new Runnable() {
//                public void run() {
//                    new DigitalKYCServer().setVisible(true);
//                }
//            });
            try{
                ss=new ServerSocket(7800);
                System.out.println("Listening:");
                while(true)
                {
//                    while(true)
//                    {
                        s=ss.accept();
                        isr=new InputStreamReader(s.getInputStream());
                        br=new BufferedReader(isr);
                        message=br.readLine();
                        if(message==null)
                            continue;
                        System.out.println(message);
//                        break;
//                    }
                    pw=new PrintWriter(s.getOutputStream());
                    pw.println("1");
                    pw.flush();
                    ObjectInputStream ois=new ObjectInputStream(s.getInputStream());
                    try{
                        byte []buffer= (byte[]) ois.readObject();
                        System.out.println("Image Recieved");
                        Imgpath=path+new SimpleDateFormat("yyyyMMdd-HHmmss").format(new Date())+".jpg";
                        FileOutputStream fos=new FileOutputStream(Imgpath);
                        fos.write(buffer);
                    }
                    catch (Exception e)
                    {
                        System.out.println("Error occured "+e);
                        System.exit(0);
                    }
//                    dis=new DataInputStream(s.getInputStream());
//                    len=dis.readInt();
//                    data=new byte[len];
//                    if(len>0)
//                        dis.readFully(data,0,data.length);
//                    BufferedImage bimg= ImageIO.read(new ObjectInputStream(s.getInputStream()));
//                    String Path="screenshot.jpg"; // Change the path here.
//                    ImageIO.write(bimg, "jpg", new File(Path));
//                    System.out.println("Image Recieved");
                    System.out.println("Image Saved");
                    //Do the Image processing here.
                    Process p;
                    try {
                        String[] cmd = { "/bin/sh","-c","/home/pramit/IdeaProjects/DigitalKYCServer/src/com/company/crop_n_rotate.py "
                                +Imgpath+" "+message};

                        p = Runtime.getRuntime().exec(cmd);
                        BufferedReader reader=new BufferedReader(new InputStreamReader(
                                p.getInputStream()));
                        p.waitFor();
//                        String z=String.valueOf(p.exitValue());
//                        System.out.println("z= "+z);
                        String line;
                        sbr=new StringBuffer("");
                        while((line = reader.readLine()) != null) {
                            System.out.println(line);
                            sbr.append(line+"\n");
                        }
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
//                    br=new BufferedReader(isr);
//                    message=br.readLine();
                    //////////////////////changed here
                    pw=new PrintWriter(s.getOutputStream());
                    pw.println(sbr.toString());
                    pw.flush();
                    pw.close();
//                    ImageIcon icon=new ImageIcon(bimg);
//                    JFrame frame=new JFrame();
//                    frame.setLayout(new FlowLayout());
//                    frame.setSize(200,300);
//                    JLabel lbl=new JLabel();
////                    lbl.setIcon(icon);
//                    frame.add(lbl);
//                    frame.setVisible(true);
                }
            }catch(IOException e)
            {
                e.printStackTrace();
            }
        }
    }
}


