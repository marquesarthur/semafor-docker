FROM msarthur/semafor-base:latest
MAINTAINER marques.s.arthur@gmail.com

EXPOSE 8085

CMD ["/usr/bin/java", \
     "-Xms4g", \
     "-Xmx4g", \
     "-cp", \
     "/semafor-master/target/Semafor-3.0-alpha-04.jar", \
     "edu.cmu.cs.lti.ark.fn.SemaforSocketServer", \
     "model-dir:/models/semafor_malt_model_20121129", \
     "port:8085"]
     