/*package com.abin.test;  */
  
import java.io.IOException;  
  
import com.rabbitmq.client.Channel;  
import com.rabbitmq.client.Connection;  
import com.rabbitmq.client.ConnectionFactory;  
  
public class Send {  
    private final static String QUEUE_NAME = "QUEUE_NAME";  
  
    public static void main(String[] args) throws IOException {  
        ConnectionFactory factory = new ConnectionFactory();  
        factory.setHost("amqp.servername);  
        Connection connection = factory.newConnection();  
        Channel channel = connection.createChannel();  
  
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);  
        String message = "test";  
        channel.basicPublish("", QUEUE_NAME, null, message.getBytes());  
        System.out.println(" [x] Sent '" + message + "'");  
  
        channel.close();  
        connection.close();  
    }  
}  