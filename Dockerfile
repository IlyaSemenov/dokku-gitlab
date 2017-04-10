FROM sameersbn/gitlab:9.0.4

EXPOSE 80
ENTRYPOINT ["/sbin/dokku-entrypoint.sh"]
CMD ["app:start"]

# Procfile interferes with Dokku
RUN rm Procfile

COPY sbin/* /sbin/

# GitLab startup time is unpredictable. Refrain from using CHECKS at the moment.
#COPY CHECKS /app/
