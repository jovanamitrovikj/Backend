from SPARQLWrapper import SPARQLWrapper, JSON
from django.shortcuts import render
from .models import SparqlResult
from django.http import JsonResponse


def sparql_result_as_json(request):
    # Query the SparqlResult model to get all data
    results = SparqlResult.objects.all()

    # Serialize the query results as JSON
    data = [result.result for result in results]

    # Create a JsonResponse with the serialized data
    return JsonResponse(data, safe=False)


def sparql_query(request):
    if request.method == 'POST':
        sparql_query_text = request.POST.get('sparqlQuery')
        endpoint_url = request.POST.get('endpoint')

        sparql = SPARQLWrapper(endpoint_url)
        sparql.setQuery(sparql_query_text)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()

            city_population_list = [
                {
                    'city': binding['city']['value'],
                    'population': binding['population']['value']
                }
                for binding in results['results']['bindings']
            ]
            SparqlResult.objects.create(result=results)

            return render(request, 'TeamProject/dashboard.html', {'city_population_list': city_population_list})
        except Exception as e:
            error_message = str(e)
            return render(request, 'TeamProject/index.html', {'error_message': error_message})

    return render(request, 'TeamProject/index.html')
