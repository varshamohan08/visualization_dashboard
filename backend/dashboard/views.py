from django.shortcuts import render
from dashboard.models import Insight
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from backend import ins_logger
import sys
from datetime import datetime

# Create your views here.
class DashBoardAPI(APIView):
    def get(self, request):
        try:
            insights = Insight.objects.values()
            return Response({"insights": insights}, status=status.HTTP_200_OK)
        except Exception as e:

            exc_type, exc_value, exc_traceback = sys.exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})

            return Response({"sucess":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                insights = request.data
                for insight_data in insights:
                    added_str = insight_data.get('added',"")
                    published_str = insight_data.get('added',"")
                    
                    # Parse datetime strings and convert to the correct format
                    if added_str != "":
                        added_datetime = datetime.strptime(added_str, "%B, %d %Y %H:%M:%S")
                    else:
                        added_datetime = None
                    if published_str != '':
                        published_datetime = datetime.strptime(published_str, "%B, %d %Y %H:%M:%S")
                    else:
                        published_datetime = None
                    Insight.objects.create(
                        end_year=insight_data.get('end_year', None),
                        intensity=insight_data.get('intensity', None) if insight_data.get('intensity', "") != "" else None,
                        sector=insight_data.get('sector', None),
                        topic=insight_data.get('topic', None),
                        insight=insight_data.get('insight', None),
                        url=insight_data.get('url', None),
                        region=insight_data.get('region', None),
                        start_year=insight_data.get('start_year', None),
                        impact=insight_data.get('impact', None),
                        added=added_datetime,
                        published=published_datetime,
                        country=insight_data.get('country', None),
                        relevance=insight_data.get('relevance', None) if insight_data.get('relevance', "") != "" else None,
                        pestle=insight_data.get('pestle', None),
                        source=insight_data.get('source', None),
                        title=insight_data.get('title', None),
                        likelihood=insight_data.get('likelihood', None) if insight_data.get('likelihood', "") != "" else None
                    )
                return Response({"success": True}, status=status.HTTP_200_OK)
        except Exception as e:

            exc_type, exc_value, exc_traceback = sys.exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})

            return Response({"sucess":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)