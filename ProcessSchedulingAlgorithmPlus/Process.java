package os;
import java.util.ArrayList;
import java.util.List;

/**
 * ������������Ľ����б�������.
 */
public class Process {

    public static List<double []> task_info=new ArrayList<>();//�����б�
    public static  int task_num=8;//������


    public static  void init_task()//��ʼ�������б�
    {
        for(int i=0;i<task_num;i++)
        {
            double[] t=new double[4];
            t[0]=i;//���̺�
            t[1]=0;//����ʱ��
            t[2]=0;//��Ӧ��
            t[3]=(int)(Math.random()*100)%20+1;//��Ҫ����ʱ��
            task_info.add(t);
        }
    }

    public static void main(String arg[])
    {
        Process.init_task();//��ʼ�������б�
        

        System.out.println("\n\n����Ӧ�����ȵ����㷨��ʼ����:");  
        HRRN.init_task(task_info,task_num);  
        HRRN.HRRN();//������ȼ�
        
        System.out.println("\n\nʱ��Ƭ��ʼ��ת��");
        RR.init_task(task_info,task_num);
        RR.CircleTime();//ʱ��Ƭ��ת

    }
}
